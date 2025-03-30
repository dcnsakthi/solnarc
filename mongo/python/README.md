# MongoDB Python Application

python -m pip install "pymongo[srv]" --upgrade

## Environment Variables

This application uses a `.env` file to store sensitive information. Below is the required configuration:

```
# MongoDB configuration
MONGO_URI=mongodb+srv://mreadmin:<db_password>@cm0mre.si8rx.mongodb.net/?retryWrites=true&w=majority&appName=CM0MRE&tls=true
```

Replace `<db_password>` with your actual MongoDB password.

## Troubleshooting

- **SSL Handshake Failed**: Ensure you are using the latest version of `pymongo` and Python.
- **TLS Version**: Verify your system supports TLS 1.2 or higher.
- **Firewall**: Ensure no firewall or network restrictions block MongoDB connections.
