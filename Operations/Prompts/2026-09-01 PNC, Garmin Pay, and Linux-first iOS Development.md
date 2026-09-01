---
title: PNC, Garmin Pay, and Linux-first iOS Development
date: 2026-09-01
tags: [prompt-log, pnc, garmin-pay, grapheneos, cachyos, thinkpad, xcode, chiron]
model: GPT-5.6 Codex
tool: Codex + web research
status: completed
---

# Prompt

PNC bank, my mom has a MAc, I use a Lenovo thinkpad, using CachyOS

# Result

PNC confirms that eligible PNC Visa debit and credit cards can be added to Garmin Pay. Therefore, a Garmin watch with Garmin Pay can meet the contactless-payment requirement on a future GrapheneOS daily driver, despite Google Wallet NFC payments being unavailable on GrapheneOS. Eligibility remains card-specific and should be verified in Garmin Connect before committing to a watch purchase.

Keep the ThinkPad/CachyOS system as the primary workstation. Build Chiron web-first/local-first there and test it in the existing iPhone browser from day one. The mother's Mac is sufficient as an occasional iOS build, signing, simulator, and physical-device-testing station; it should not be relied on for everyday work. Expo documents that Linux developers need a physical iOS device for iOS testing, while the iOS Simulator requires macOS. If native iOS release work becomes routine, procure independent Mac access (a Mac mini is the natural low-cost option) only after a product is shipping and the access bottleneck is demonstrated.

The phone plan remains: retain the working iPhone 16 Pro now; wait for 2027 Motorola official GrapheneOS hardware rather than buying an interim Pixel. Treat the future Motorola as a candidate to test, not a preorder commitment.

Sources consulted: PNC Garmin Pay documentation; Garmin participating-bank list; Apple Xcode system requirements; Expo iOS Simulator documentation.
