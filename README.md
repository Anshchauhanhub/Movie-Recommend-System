# 🎬 Movie Recommender System

This repository contains a Movie Recommender System built with Streamlit. The app allows users to select a movie and get recommendations for similar movies, along with their posters.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/movierecommender.git
   cd movierecommender
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download the `movies_dict.pkl` file and place it in the project directory.

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and go to [http://localhost:8501](http://localhost:8501) to access the app.

3. Select a movie from the dropdown menu in the sidebar and adjust the number of recommendations using the slider.

4. Click the "Recommend" button to see the recommended movies along with their posters.

## Features

- Select a movie from a dropdown menu
- Get recommendations for similar movies
- Display movie posters and titles in a card-like layout

## Project Structure
```
movierecommender/
├── app.py                # Main Streamlit app
├── movies_dict.pkl       # Pickle file containing movie data
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
