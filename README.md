# credit-card-validation

Welcome to the Credit Card Validation System. This application is built using React for the front-end and FastAPI for the back-end. It allows you to check if a Credit Card is valid.

## Requirements

- Node.js and npm (for the React front-end)
- Python 3.7+ (for the FastAPI back-end)

## Installation

1. Clone the repository to your local machine

```bash
git clone https://github.com/felipneiva/credit-card-validation
```

2. Navigate to the project's root directory:

```bash
cd credit-card-validation
```

3. Install the dependencies for both the front-end and back-end:

```bash
# Install front-end dependencies (from the client directory)
cd client
npm install

# Install back-end dependencies (from the server directory)
cd ../server
pip install -r requirements.txt
```
## Usage

1. Start the FastAPI server:

```bash
# From the server directory
cd server
uvicorn main:app --reload
```

2. Start the React front-end development server:

```bash
# From the client directory
cd ../client
npm run dev
```
3. Access the application in your web browser at http://localhost:5173.
4. Enter a credit card in the input fields and click the "Submit" button to see the results.

