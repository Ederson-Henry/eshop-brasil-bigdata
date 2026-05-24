```yml
version: '3.9'

services:
  mongodb:
    image: mongo:latest
    container_name: mongodb_eshop
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_DATABASE: eshop

  streamlit:
    build: .
    container_name: streamlit_eshop
    ports:
      - "8501:8501"
    depends_on:
      - mongodb
