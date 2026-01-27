# NambaTech

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Frappe](https://img.shields.io/badge/Frappe-v15-blue)](https://frappe.io)

> **Release: Artemis v1.0.0** 🚀

A custom Frappe application for managing the **nambatech.com** e-commerce platform - Kenya's premier marketplace for quality refurbished electronics.

## 🎯 About

NambaTech is a comprehensive e-commerce solution built on the Frappe framework, designed specifically for selling refurbished electronics in Kenya. The platform provides:

- **Product Management** - Manage electronics inventory with detailed specifications
- **Order Processing** - Streamlined order workflow from cart to delivery
- **Customer Management** - Customer profiles, wishlists, and purchase history
- **Payment Integration** - Support for Kenyan payment methods
- **Delivery Tracking** - Real-time order tracking and delivery management

## 🛠️ Tech Stack

- **Framework**: [Frappe](https://frappe.io) v15
- **Backend**: Python 3.10+
- **Frontend**: JavaScript, HTML, CSS
- **Database**: MariaDB

## 📦 Installation

### Prerequisites

- Python 3.10 or higher
- [Frappe Bench](https://github.com/frappe/bench) installed and configured
- MariaDB 10.6+

### Setup

1. **Get the app**
   ```bash
   cd $PATH_TO_YOUR_BENCH
   bench get-app https://github.com/recorner/nambatech --branch main
   ```

2. **Install on your site**
   ```bash
   bench --site your-site.local install-app nambatech
   ```

3. **Run migrations**
   ```bash
   bench --site your-site.local migrate
   ```

## 🧑‍💻 Development

### Setting Up Development Environment

```bash
cd apps/nambatech

# Install pre-commit hooks
pre-commit install
```

### Code Quality Tools

This app uses the following tools for code quality:

- **ruff** - Python linting and formatting
- **eslint** - JavaScript linting
- **prettier** - Code formatting
- **pyupgrade** - Python syntax upgrades

### Running Tests

```bash
bench --site your-site.local run-tests --app nambatech
```

## 🔄 CI/CD

GitHub Actions workflows are configured for:

- **CI** - Runs unit tests on every push to `main` and `develop` branches
- **Linters** - Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on pull requests

## 📁 Project Structure

```
nambatech/
├── nambatech/           # Main app module
│   ├── config/          # App configuration
│   ├── public/          # Static assets (CSS, JS)
│   ├── templates/       # Jinja templates
│   └── www/             # Web pages
├── .github/             # GitHub workflows
├── pyproject.toml       # Project configuration
└── README.md
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](license.txt) file for details.

## 👥 Author

**NambaTech Team**
- Email: westronet@gmail.com
- GitHub: [@recorner](https://github.com/recorner)

## 🌐 Links

- **Website**: [nambatech.com](https://nambatech.com)
- **Documentation**: Coming soon
- **Issues**: [GitHub Issues](https://github.com/recorner/nambatech/issues)

---

<p align="center">Made with ❤️ in Kenya 🇰🇪</p>
