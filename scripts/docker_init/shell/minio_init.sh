#!/bin/sh
set -e

echo "Waiting for MinIO to be ready ..."
mc alias set local "http://minio:9000" "$MINIO_ROOT_USER" "$MINIO_ROOT_PASSWORD"

echo "Creating buckets ..."
mc mb --ignore-existing "local/$MINIO_BRONZE_BUCKET"

echo "✅ Init MinIO successfully finished"