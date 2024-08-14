# House Price Prediction

Welcome to the House Price Prediction web application! This project is designed to predict the price of houses based on various factors such as the number of bedrooms, bathrooms, house size, and location. The project includes a Flask-based backend and a stylish frontend for user interaction.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Features](#features)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.2 - 3.8+
- pip
- Virtual environment (optional but recommended)

### Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/house-price-prediction.git
   cd house-price-prediction
   ```

2. **Create a Virtual Environment (Optional)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask Application**
   ```bash
   python app.py
   ```

5. **Access the Application**
   Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

### Web Interface

1. **Homepage**: You will be greeted by a visually appealing page where you can input details like the number of bedrooms, bathrooms, size, and zip code.

2. **Prediction**: After filling in the details, click on the "Predict Price" button to get the estimated house price. The result will be displayed on the same page.

### API Interface

If you prefer interacting with the application programmatically, you can use the `/predict` API endpoint.

#### Example Request:

```bash
curl -X POST -F "beds=3" -F "baths=2" -F "size=1500" -F "zip_code=98001" http://127.0.0.1:5000/predict
```

#### Example Response:

```json
{
    "price": "INR 5,500,000"
}
```

## Project Structure

```
house-price-prediction/
│
├── app.py                # Main Flask application file
├── templates/
│   └── index.html        # Frontend HTML file
├── House price prediction.ipynb  # Jupyter Notebook for model training and analysis
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Features

- **Responsive UI**: A stylish and responsive user interface for easy interaction.
- **Real-Time Prediction**: Get instant predictions for house prices based on user input.
- **Data-Driven**: Uses a machine learning model trained on real housing data.

## API Endpoints

- **`/`**: The main page to input house details.
- **`/predict`**: POST endpoint to predict the house price based on input features.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or raise an Issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

You can customize this `README.md` further to suit your needs.
