# Security Policy

## Supported Versions

| Version | Supported          |
|---------|--------------------|
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

We take the security of StudentAI seriously. If you discover a security vulnerability, please follow these steps:

1. **Do not** open a public issue on the issue tracker.
2. Send a description of the vulnerability to the project maintainers via a private channel.
3. Include steps to reproduce the issue and any relevant code snippets.
4. Allow time for the vulnerability to be addressed before public disclosure.

### What to expect

- **Acknowledgment:** You will receive acknowledgment of your report within 48 hours.
- **Updates:** We will provide updates on the status of the fix.
- **Disclosure:** Once fixed, we will publicly acknowledge the report (with your permission).

## Security Best Practices

- This application runs **entirely locally** — no data is sent to external servers.
- No API keys, tokens, or credentials are required.
- All PDF processing and model inference occurs on your machine.
- Keep your dependencies updated to receive the latest security patches:

```bash
uv sync --all-groups --upgrade
```

## Known Security Considerations

- The application does not implement authentication or authorization — it is designed for local use only.
- Do not expose the Streamlit server to untrusted networks.
- Always run the application in a trusted environment.
