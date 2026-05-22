import os
import random

import torch
from PIL import Image
from sentence_transformers import SentenceTransformer

from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from tqdm import tqdm

device = 'cpu'

model = SentenceTransformer(
    'jinaai/jina-clip-v2',
    trust_remote_code=True,
    truncate_dim=1024,
    device=device
)
images = [os.path.join('images', f) for f in os.listdir('images')]

# 1. ALWAYS initialize the client first
client = QdrantClient(path='image_store')

# 2. Check if the collection actually exists inside the database
collection_exists = any(c.name == 'images' for c in client.get_collections().collections)

if not collection_exists:
    print("Collection 'images' not found. Creating embeddings...")
    images = [os.path.join('images', f) for f in os.listdir('images')]
    
    # Use the faster batch encoding
    embeddings = model.encode(
        images, 
        batch_size=16, 
        show_progress_bar=True, 
        normalize_embeddings=True, 
        device=device
    )

    client.recreate_collection(
        collection_name='images',
        vectors_config=VectorParams(size=len(embeddings[0]), distance=Distance.COSINE)
    )

    client.upsert(
        collection_name='images',
        points=[
            PointStruct(id=i, vector=embeddings[i].tolist(), payload={'path': images[i]})
            for i in range(len(images))
        ]
    )
    print("Collection created successfully!")

# 3. Now the query will work because the client is connected and collection exists
print('Done. Ready to search.')
search_query = input('Enter search query: ')

embedded_query = model.encode(search_query, normalize_embeddings=True, device=device)

results = client.query_points(collection_name='images', query=embedded_query, limit=3).points

print([r.payload['path'] for r in results])