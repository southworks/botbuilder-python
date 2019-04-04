# Roadmap proposal

This page provides a roadmap for the v4 SDK. Bot Builder v4 SDK builds on the feedback and learnings from the prior Bot Builder SDKs. It introduces the right levels of abstraction while enabling rich componentization of the bot building blocks. You can start with a simple bot and grow your bot in sophistication using a modular and extensible framework.

Legend of annotations: 

| Mark | Description |
| --------- | ------- |
| bullet | backlog |
| check mark | completed |
| :runner: | work in progress |
| :muscle: | stretch goal |
| :triangular_flag_on_post: | postponed |

## [Timeframe] 2019

### (1) Infrastructure [half green] 
- build [half green]
- packaging publishing [half green]
- test automation [green]
- code coverage tooling [half red]

### (1) Conectivity [3 weeks]
- connector / schema [green]
- adapter [empty red] + middleware [empty green]
- OAuth support & gov [empty red]
  - revamp auth (adal)
  
### (2) Samples [3 weeks]
- notebooks
- spacy as multiple intent recognizer
- luis sample
- add john's spacy sample
- update current samples

### (3) Luis & QnA [red] [1 week]

### (4) Dialogs + Prompts [red] [2 weeks]

### (4) Azure (Cosmos & Blob) [red] [1 week]

### (4) Timex [half red] [1 week]

### (5) Telemetry [red] [2 weeks]
- transcript
- app insights

### (?) Docs [red] [2 weeks]


----------------------------------------------------------------



## December 2018 (4.2.x) 
- Regression tests across Python
- Date time lib for Python
- Regression tests across Python
- Date time lib for Python
- LUIS and QnA recognizer for Python
- Final docs, samples and UA content

## August 2018
- [x] Stabilization, bug fixes

## July 2018
- [x] close gaps between C#, JS, :triangular_flag_on_post: Python, :triangular_flag_on_post: Python
- [x] Proactive messaging cleanup
- [x] Prompts and dialog cleanup, DCRs

## June 2018 
- [x] State management revamp
- [x] Code cleanup
- [x] OAuth for Python
- [x] Perf improvements
- :triangular_flag_on_post: Middleware infrastructure for Python

## May 2018 (M5: broad public preview)
- [x] Unit test framework, tests for core functionality
- [x] Initial docs & UA content
- [x] Integration tests
- [x] V4 conceptual SDK docs
- :triangular_flag_on_post: Improved state management and potential DCR for state management 
- [x] Add OAthu support for V4
- [x] Align connectors across languages
- [x] Lift and shift of v3 to v4 (C#)
- :triangular_flag_on_post: Lift and shift of v3 to v4 (JS)
- :muscle: Python and Java language parity for Middleware, Prompts, Dialogs, Storage, and State Management.

## April 2018 (M3: v3 to v4 migration, new functionality and API freeze)
- [x] V3 -> V4 migration helpers for C#
- [x] V3 -> v4 migration docs for C#
- [x] V4 samples (partial)
- [x] Finalize intent & entity recognizers
- [x] Final APIs, bug fixes and polish (preview release quality)
- [x] Dialogs in C#
- :triangular_flag_on_post: LUIS, QnA client (Python)

## March 2018 (M2: Securing the architecture)
- [x] Publish Java packages
- [x] Finalize specs for Intent & Entity format, (:triangular_flag_on_post:) Analytics 
- [x] Support for Invoke activity - C#
- [x] Datetime, choice prompts in C#
- [x] Finalize state
- [x] Support for Invoke activity - JS
- [x] Java SDK (Feature parity with 2/9 C# and Node feature set)
- [x] Factored code to match desired architecture
- [x] Finalize context
- [x] Python SDK (Feature parity with 2/9 C# and Node feature set)
- [x] Async-await for Python SDK
- [x] TIMEX (C# and JS SDK)

## February 2018 (M1: Public GitHub repos)
- [x] Connector + adapter
- [x] Initial Samples
- [x] Initial Docs (Wiki)
