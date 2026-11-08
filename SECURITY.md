# Security and privacy

Device uploads use a source-specific random key and an allowed direct LAN subnet. Keys authorize uploads only. HA stores their SHA256 digest, not plaintext. The browser endpoints separately require an authenticated HA administrator; the static JavaScript contains no credentials.

The LAN policy rejects known Nabu Casa requests, forwarding headers and a mismatch between the socket peer and request remote address. It is application-level filtering, not a firewall. Remote routing and middleware still require testing on the supported HA version. Do not bypass these restrictions to make a device upload work.

Audio is stored as ordinary WAV files in the configured media directory, not encrypted by this integration. HA media permissions also apply; the files are not an isolated per-user mailbox. Protect backups and storage access. Uploads over HTTP expose audio and the device key to anyone able to observe that network traffic.

Limits: 60 seconds, 8 MiB/request, 100 WAV files globally, 32 MiB disk reserve, two simultaneous uploads and one per source, 30-second receive timeout. Five invalid-key attempts within 60 seconds block an IP; 50 globally block authentication. No automatic deletion or key logging.

Do not put secrets or recordings into issues. If GitHub private vulnerability reporting is enabled, use the repository's Security tab. Otherwise contact the maintainer privately before disclosing a credential-related problem. No response-time guarantee is made.
