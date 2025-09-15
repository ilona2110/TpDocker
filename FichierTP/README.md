
## Commandes Git pour créer le dépôt

```bash
# Créer la structure des dossiers
mkdir -p mon-depot-tp/TP-Docker

# Se placer dans le dossier principal
cd mon-depot-tp

# Créer les fichiers README.md (copier le contenu ci-dessus)
# README.md principal et TP-Docker/README.md

# Initialiser le dépôt Git
git init
git add .
git commit -m "Initial commit: TP Docker - Hello World"

# Ajouter le remote et pousser
git remote add origin [URL_DE_VOTRE_DEPOT]
git push -u origin main

## Setup Instructions

1. **Clone the repository** (if applicable):
   ```
   git clone <repository-url>
   cd flask-mongo-app
   ```

2. **Build and run the application using Docker Compose**:
   ```
   docker-compose up --build
   ```

3. **Access the application**:
   Open your web browser and go to `http://localhost:5000`. You should see a "Hello World!" message indicating that the Flask application is running.

## Usage

- The application has a single route (`/`) that returns a simple HTML message.
- The application is configured to connect to a MongoDB database. Ensure that the MongoDB service is running and accessible.

## Dependencies

The project requires the following Python packages:

- Flask
- PyMongo

These dependencies are listed in the `requirements.txt` file and will be installed automatically when building the Docker image.

## License

This project is licensed under the MIT License.