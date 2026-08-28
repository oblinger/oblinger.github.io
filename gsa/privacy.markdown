---
layout: cayman
title: Privacy Policy — Google Suite Access (gsa)
description: How the gsa command-line tool handles data. Last updated 27 August 2026.
permalink: /gsa/privacy/
---

*Last updated: 27 August 2026*

## Summary

**`gsa` is a single-user command-line tool.** It runs on its author's own computer, accesses only the Google account that authorizes it, and sends data to no one.

## Who operates this tool

Dan Oblinger, operating it personally. Contact: **oblinger@gmail.com**.

## What data is accessed

When you authorize `gsa`, it can read and write Google Docs, Sheets, Slides and Drive files in your account, read Gmail messages, and access Calendar, Tasks, Contacts, Forms and Chat data. It accesses these only when a command is explicitly run, and only for the account that granted consent.

## What data is stored

`gsa` stores exactly one thing: the OAuth credential Google issues at authorization, written to a private file on the local machine, readable only by the operating-system user who authorized it. Document contents are printed to the terminal or written where the command directs, and are not retained by the tool itself.

## What data is transmitted

Only to Google. `gsa` communicates with Google's own API endpoints and with nothing else. There are no analytics, no telemetry, no logging service, no third-party processors, and no server operated by the author. Data is never sold, shared, or transferred to anyone.

## Retention and deletion

The stored credential remains until deleted. To remove it, delete the credential file on the machine. To revoke the tool's access entirely, visit [Google Account permissions](https://myaccount.google.com/permissions) and remove it — this takes effect immediately and independently of anything on the local machine.

## Google API Services User Data Policy

The use of information received from Google APIs adheres to the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy), including the Limited Use requirements.

## Changes

Changes to this policy will be posted on this page with a revised date.

## Contact

Questions: **oblinger@gmail.com**
