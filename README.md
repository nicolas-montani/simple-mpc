# Simple MPC (Multi-Party Computation)

This project was developed in collaboration with the **Cybersecurity Chair of the University of St. Gallen**.

## Project Overview

This repository contains implementations of Multi-Party Computation (MPC) protocols, specifically focusing on Shamir's Secret Sharing scheme. The project demonstrates secure computation techniques that allow multiple parties to jointly compute functions over their inputs while keeping those inputs private.

## Project Structure

The repository is organized into several versions and components:

- **MPC/**: Initial implementation with socket server architecture
- **MPC2.0/**: Enhanced version with Flask web application and improved database handling
- **MPC2.1/**: Refined implementation with updated client-server architecture
- **MPC3/**: Latest version with optimized performance and features

Each version includes:
- Client implementations for secret sharing and reconstruction
- Flask web applications for user interaction
- Database handlers for persistent storage
- Docker configurations for easy deployment

## Key Features

- **Shamir's Secret Sharing**: Implementation of threshold secret sharing scheme
- **Web Interface**: Flask-based web applications for easy interaction
- **API Endpoints**: RESTful APIs for programmatic access
- **Containerization**: Docker support for consistent deployment
- **Database Integration**: Persistent storage for shares and computation results

## Academic Collaboration

This work represents a collaborative effort with the Cybersecurity Chair at the University of St. Gallen, contributing to research and education in the field of secure multi-party computation and applied cryptography.

## Technologies Used

- Python
- Flask
- Docker
- Cryptographic libraries for MPC implementations
- RESTful API design

---

*This project serves both educational and research purposes in the domain of secure computation and privacy-preserving technologies.*
