<div align="center">

  <img src="artifacts/stocks.jpeg" alt="logo" width="300" height="auto" />
  <h1>Google Finance Stocks Info</h1>
  
  <p>
    Get realtime and historical securities information in JSON from Google Finance using the Google Sheets and Drive APIs. 
  </p>
</div>

<!-- Table of Contents -->
# Table of Contents
- [About the Project](#about-the-project)
  * [Screenshots](#screenshots)
  * [Tech Stack](#tech-stack)
  * [Features](#features)
- [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Running Tests](#running-tests)
  * [Run Locally](#run-locally)
  * [Deployment](#deployment)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
  * [Code of Conduct](#code-of-conduct)
- [FAQ](#faq)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

<!-- About the Project -->
## About the Project
Unfortunately the "Google Finance API (both the Portfolio API and the Finance Gadgets and Tools API)" were "<a href="https://groups.google.com/g/google-finance-apis">shut down</a> on October 20, 2012". Realtime and historical data can be retrieved though using the <a href="https://support.google.com/docs/answer/3093281?hl=en">=GOOGLEFINANCE()</a> function directly in Google Sheets.
This project creates programmatically a spreadsheet and populates the required information using the GOOGLEFINANCE. Values are then retrieved and served as a JSON response using FastAPI.

<!-- Screenshots -->
### Screenshots

<div align="center"> 
  <img src="artifacts/google-finance-stocks-info-screenshot.png" alt="logo" width="auto" height="auto" />
</div>

<!-- TechStack -->
### Tech Stack

<details>
  <ul>
    <li><a href="https://www.python.org/">Python 3</a></li>
    <li><a href="https://fastapi.tiangolo.com/">FastAPI</a></li>
    <li><a href="https://developers.google.com/sheets/api/quickstart/python">Sheets API</a></li>
    <li><a href="https://www.docker.com/">Docker</a></li>
  </ul>
</details>

<!-- Features -->
### Features

- For realtime data retrieves: price, priceopen, high, low, volume, marketcap, tradetime, datadelay, volumeavg, pe, eps, high52, low52, change, beta, changepct, closeyest, shares, and currency information.
- For historical data retrieves: open, close, high, low, and volume information.

<!-- Getting Started -->
## Getting Started
Clone the <a href="https://github.com/andreihalici/googlefinance-stocks-info">googlefinance-stocks-info</a> repository locally.

<!-- Prerequisites -->
### Prerequisites


<!-- Authentication & authorization -->
### Authentication & authorization

