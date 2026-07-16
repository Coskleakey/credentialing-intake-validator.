
# Medical Credentialing Data Validator 🩺

A lightweight Python data-validation layer built with Pydantic to solve the "Document Scavenger Hunt" and manual data-entry errors in medical provider onboarding.

## The Problem
In US healthcare administration, credentialing specialists waste hours manually copy-pasting National Provider Identifier (NPI) numbers, DEA codes, and expiration dates from messy provider emails into Excel sheets. A single alphanumeric typo (like swapping an `8` for a `B`) results in immediate payer rejections, resetting the 90-day insurance billing clock and stalling clinic revenue.

## The Solution
This repository contains the core Pydantic data schemas designed to act as a strict gatekeeper for AI-extracted document data. By utilizing Python's `Literal` and `datetime` types, it programmatically blocks malformed data and inconsistent text casing before it can ever corrupt a database or dashboard.

## Tech Stack
- Python 3.10+
- Pydantic v2
