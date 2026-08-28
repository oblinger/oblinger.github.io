---
layout: cayman
title: Google Suite Access (gsa)
description: A single-user command-line tool for reading and writing the author's own Google Workspace documents.
permalink: /gsa/
---

## What this is

**Google Suite Access (`gsa`)** is a small command-line utility written by Dan Oblinger for his own use. It reads and writes Google Docs, Sheets, Slides and Drive files, and searches Gmail, on behalf of the single Google account that authorizes it.

It exists so that automation running on the author's own computer can work with his own documents. It is not a product, not a service, and has no users other than the author.

## How it works

`gsa` runs locally on the author's machine. It authorizes once through Google's standard OAuth consent flow, stores the resulting credential in a private file on that machine, and then calls Google's public APIs directly. There is no server, no hosted component, and no account system.

## Scope of access

The tool requests access to Google Docs, Sheets, Slides, Drive, Gmail, Calendar, Tasks, Contacts, Forms and Chat for the authorizing account. In practice it exercises the Docs, Sheets, Slides, Drive and Gmail-read portions; the remainder is requested so that authorization does not have to be repeated as the tool grows.

## More

- [Privacy policy](/gsa/privacy/)
- [Terms of service](/gsa/terms/)
