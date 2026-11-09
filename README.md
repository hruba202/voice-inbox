<img width="1892" height="947" alt="voice01" src="https://github.com/user-attachments/assets/e1538cae-1a12-4de1-88f8-359084dea15c" />

# Voice Inbox for Home Assistant

Record a short voice message in your browser or upload audio from an ESPHome device, and keep the WAV recording in Home Assistant's media directory.

Created by **hruba202 with assistance from OpenAI ChatGPT / Codex**.
- You can use the voice inbox with this doorbell integration, for which it was created:
- https://github.com/hruba202/p4-doorbell
## Status

Version 0.3.2 packages the existing 0.3.1 integration for HACS / Marketplace. Recording from a browser and an ESP32-P4 has been reported working by the project owner. The new package still needs a clean-install and update test; it is **not yet approved for the public Marketplace catalog**. See [VALIDATION.md](VALIDATION.md).

The intended repository is `hruba202/voice-inbox`; links below become usable after it is published. The configuration form supports English and Czech. The recorder panel, entity names and quota notifications currently use Czech.

## Features

- Browser recording with Start, Stop and save, Cancel, and playback of the saved message.
- Separate upload sources with individual keys and LAN restrictions.
- PCM / WAV input: signed 16-bit mono, 16 or 48 kHz, maximum 60 seconds and 8 MiB per request.
- Atomic WAV storage under `<media-directory>/vzkazy/<source>/`.
- Last-message sensor, total count, shared quota usage and quota warning entity.
- Events after successful storage and on quota warnings/rejections.
- 100 WAV files across all sources; warning at 80%, rejection at capacity. **No automatic deletion.**

VoIP Stack, a particular ESP32 board, speech recognition and cloud transcription are not required. This integration does not start the microphone of an ESP device or provide telephone calls; firmware sends its own completed recording.

## Install

Requires Home Assistant **2026.10.3 or newer** and a writable configured media directory. Compatibility with later releases must be verified; see the validation status.

1. In Marketplace (or HACS), add `https://github.com/hruba202/voice-inbox` as a custom repository, category **Integration**.
2. Download Voice Inbox and restart Home Assistant.
3. Go to **Settings → Devices & services → Add integration → Voice Inbox**.
4. Configure a source ID, allowed LAN subnet and a unique upload key.
5. As an administrator, open **Hlasové vzkazy** in the sidebar (or `/voice-inbox`).

Manual alternative: copy only `custom_components/voice_inbox` into your HA configuration's `custom_components` folder, then restart. This is an integration, not an app/add-on.

### Source settings

- Source: for example `front_door`; 1–32 lowercase letters, digits, `_` or `-`, starting with a letter.
- Network: strict CIDR, for example `192.168.1.0/24`. For a single device use `192.168.1.87/32`; `192.168.1.87/24` is not a network address.
- Key: **64 random lowercase hexadecimal characters**, different for every source. Only its SHA256 digest is stored in the integration. Keep the original key in your device's secret configuration. Never publish it.

The integration prefers `/media` regardless of its HA media identifier; otherwise it uses the configured `local` directory or the sole configured media directory. Ambiguous configuration fails setup. Audio appears in **Media → My media → vzkazy**; the precise label depends on your media configuration.

## Try it without scripts

Open Home Assistant through HTTPS (for example your Nabu Casa address), sign in as an administrator, then:

1. Open **Hlasové vzkazy**, select a source and press **Nahrát vzkaz**.
2. Allow microphone access, speak, then press **Zastavit a uložit**.
3. Check **Uloženo v HA**, then play the saved file below.

This uses the microphone of the computer/phone displaying HA, **not the ESP microphone**. Recording automatically stops and uploads at 60 seconds. Keep the page open until saving finishes. Cancel discards the browser recording. Browser access requires HA administrator authentication and can work through Nabu Casa; it does not exercise the device key or LAN restrictions.

## Device uploads

Send `POST /api/voice_inbox/upload` directly to HA on the allowed LAN. Required headers:

| Header | Value |
|---|---|
| `X-Voice-Source` | Configured source ID |
| `X-Voice-Key` | Key for that source |
| `X-Audio-Rate` | `16000` or `48000` |
| `X-Audio-Bits` | `16` |
| `X-Audio-Channels` | `1` |
| `Content-Type` | `audio/wav` or `application/octet-stream` |
| `Content-Length` | Exact byte length; chunked uploads are rejected |

Raw PCM must be signed **little-endian** 16-bit mono. WAV metadata must match the headers. A successful response is **201** JSON containing `source`, `file`, `relative_path`, `duration`, `sample_rate`, `time`, `bytes` and `media_content_id`.

Errors are JSON with an `error` code: **400** malformed input, **401** access/key rejected, **413** size/duration exceeded, **415** unsupported audio, **503** busy/unavailable/rate-limited, **507** quota or disk capacity. Do not treat any non-201 response as a saved message.

Only direct LAN device uploads are accepted. Nabu Casa connections and requests with forwarding headers are rejected by this endpoint. Do not place it behind a reverse proxy or expose the HA port to the Internet as a workaround. Over plain HTTP, device audio and the upload key are not encrypted: use a trusted LAN or appropriately configured HTTPS.

After **5 wrong keys from an IP within 60 seconds**, that IP is blocked even with the correct key: **503 `authentication_rate_limited`**, `Retry-After: 60`. Wait a full 60 seconds before retrying when debugging ESP. A shared limit also blocks authentication after 50 failures within 60 seconds. These protections are not configurable in this release.

## Events and limits

`voice_inbox_saved` carries the same metadata as the 201 response, including a `media_content_id` usable by HA media actions. It never contains the audio or upload key.

`voice_inbox_quota_warning` reports `count` and `limit`; `voice_inbox_quota_rejected` reports the rejected source and quota status. Persistent notifications also warn about capacity. The limit is shared by all sources, not 100 messages per device. At most two uploads run concurrently, and only one per source. There is no listened/unlistened tracking or retention policy.

Back up `vzkazy` separately and review messages before manually deleting any. Removing a configured source does not delete its WAV files; existing files continue to count toward the quota.

## Updating the existing project installation

The domain remains `voice_inbox`. Keep existing sources, keys and recordings. Back up HA and the media directory, install the integration files, then **restart HA fully** and refresh the browser. Do not remove/recreate the config entries. The API, storage paths, entity unique IDs and config-entry version are unchanged in 0.3.2.

Rollback: restore the previous integration files and restart HA. Recorded media is outside the integration directory and is not part of Marketplace updates. Never install two copies of the same domain.

## Development and support

See [DEVELOPMENT.md](DEVELOPMENT.md), [SECURITY.md](SECURITY.md), [CHANGELOG.md](CHANGELOG.md) and [PUBLISHING.md](PUBLISHING.md). Report reproducible problems without upload keys, HA tokens or private recordings. This is a community project, not an official Home Assistant integration.


