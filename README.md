# Flask Toolbox

Flask Toolbox is a collection of tools built using Flask, a micro web framework for Python. This project includes (at least for now) two main tools: an Email and Phone Number Extractor and a URL Shortener. These tools are designed to assist users in extracting email addresses and phone numbers from a given text, as well as shortening long URLs for sharing.

## Features

1. **Email and Phone Number Extractor:**
   - Extracts email addresses and phone numbers from a given text.
   - Specifically designed for Tunisian phone numbers (+216) but can extract other country's 8-digit phone numbers.

2. **URL Shortener:**
   - Shortens long URLs using the TinyURL service.
   - Provides a shortened URL for easier sharing.

## Getting Started

### Prerequisites

- Python 3.x
- Flask framework

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/flask-toolbox.git
   cd flask-toolbox
   ```

2. **Install Flask:**

   Make sure you have Flask installed. If not, you can install it using:

   ```bash
   pip install flask
   ```

3. **Run the App:**

   To launch the Flask app, run the following command:

   ```bash
   python app.py
   ```

   This will start the development server. Open your web browser and go to `http://localhost:5000` to access the app.

4. **Explore the Tools:**

   Once the app is running, you'll see a list of tools available. Click on the links to access and use the different tools provided by the app.

6. **Access the Tools:**

   Open a web browser and navigate to the following URLs to access the different tools:

   - **Email and Phone Number Extractor:**

     Visit `http://localhost:5000/extractor` in your web browser. You'll be presented with a web page where you can paste a text containing email addresses and phone numbers.

   - **URL Shortener:**

     Visit `http://localhost:5000/urlShortener` in your web browser. You'll see an input field where you can enter a long URL that you want to shorten.

7. **Using the Tools:**

   - **Email and Phone Number Extractor:**

     1. Paste the text containing email addresses and phone numbers into the provided textarea.
     2. Click the "Extract" button to extract and display the email addresses and phone numbers.

   - **URL Shortener:**

     1. Enter the URL you want to shorten into the input field.
     2. Click the "Shorten URL" button to generate a shortened URL.

Remember to keep the terminal or command prompt open while you're using the app. You can stop the app at any time by pressing `Ctrl+C` in the terminal.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them thoroughly.
4. Submit a pull request describing your changes.

## Contact

For any inquiries or suggestions, please contact:

  [aminehidri44@gmail.com](mailto:aminehidri44@gmail.com) - [GitHub Profile](https://github.com/hidriamin)

---

## Note

This app does not require a `requirements.txt` file. However, ensure that you have Flask and other necessary dependencies installed in your Python environment before running the app.

