## Overview

**Web-Scraping-Selenium** is a Python project designed to automate the extraction of data from websites (here, **Amazon.in**) using Selenium. This repository provides scripts that demonstrate how to collect and process web data efficiently using browser automation.

## Features

- Automates web browser interactions for data collection
- Written entirely in Python
- Modular scripts for easy customization and extension

## Installation

Before using the project files, ensure you have the necessary libraries installed in your Visual Studio Code **virtual environment**. Open your terminal in VS Code and run the following commands:
- pip install selenium
- pip install bs4
- pip install pandas

These commands will install:
- **selenium**: For browser automation and web scraping
- **bs4**: For parsing HTML with Beautiful Soup
- **pandas**: For data manipulation and analysis

## Using Proxy Servers (Webshare)

To enhance the reliability and anonymity of your web scraping activities, this project supports the use of proxy servers. Integrating proxies helps you extract data from websites without getting traced or banned. 

**Why Use Proxies?**
- Proxies mask your real IP address, protecting your identity and reducing the risk of IP bans.
- They enable you to bypass geo-restrictions and access region-specific content.

**Webshare Proxy Integration**

This project recommends using [Webshare](https://www.webshare.io/) proxies for web scraping. Webshare offers a wide range of high-quality residential and datacenter proxies, which are ideal for accessing websites securely and anonymously. Webshare also provides a user-friendly dashboard, flexible authentication options, and global coverage, allowing you to select proxies from various countries as needed.

**Getting Started with Webshare Proxies**
1. Sign up for a free or paid plan on the Webshare website.
2. Choose your preferred proxy type (residential or datacenter) and location.
3. Configure your authentication method (username/password or IP whitelisting).
4. Download your proxy list or copy the proxy credentials.

## Project Structure

| File        | Description                             |
|-------------|-----------------------------------------|
| collect.py  | Main web scraping automation script      |
| project.py  | Supplementary functions and logic        |
