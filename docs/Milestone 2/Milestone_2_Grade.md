# Milestone 2 Grade — Venture 4: Krusty Compost Crew (Binny & Bloom)

**Graded:** April 8, 2026
**Deadline:** April 5, 2026 (end of day)
**Late Commits:** None — all commits are on or before 4/5/2026.

---

## Overall Grade: 84/100

---

## Summary

Binny & Bloom delivers a functional pantry-aware recipe assistant with login, inventory management (quantities, units, expiry dates), AI-powered recipe generation via OpenRouter, a recipe validator integrated into the Flask web path, and a scoring/gamification system for use/donate/compost actions. Both CLI and web GUI versions work. The validator checks for expired ingredients, pantry existence with fuzzy matching, and quantity validation. However, unit conversion still has notable failures (6/20 evaluation test cases fail), `.env.example` is missing despite being listed as a "must fix" item, the demo script is weak, and `generator.py` is an empty file.

### Video Review Notes
Venture 4 did not submit a Milestone 2 demo video. The code review suggests the system is functional with both CLI and web GUI paths working. Please ensure a demo video is included for the final presentation.

---

## Category Breakdown

### 1. End-to-End Demo Path (23/25)
- Login → view pantry → chat with AI → validated recipe or rejection → save recipe flow works end-to-end. ✓
- Validator is integrated into Flask web path (not just console) — a key Milestone 2 fix. ✓
- Inventory shows quantities, units, measurement types, and expiry dates. ✓
- Expiry prioritization built into the system prompt and context. ✓
- Both CLI (`main.py`) and GUI (`app.py`) versions work. ✓
- **Issue:** 6/20 evaluation test cases fail, mostly due to unit conversion mismatches (tbsp vs ml, etc.).
- **Issue:** Chat window closes after recipe generation (acknowledged in known issues).

### 2. Code Quality & Architecture (17/20)
- Clean Flask app with session management, hashed passwords, and `@login_required` decorator.
- `recipe_validator` class with ingredient normalization, fuzzy matching, and quantity validation.
- Unit conversion module supporting weight and volume conversions.
- OpenRouter API integration with structured JSON output enforcement.
- Expiry categorization (expired/about-to-expire/fresh) built into context.
- Score gamification system with use/donate/compost/delete actions.
- **Issue:** `generator.py` is empty — generation logic scattered across `openrouterllm.py` and `app.py`.
- **Issue:** `sort_inventory()` in `expiry.py` queries ALL inventory items, not filtered by player_id.
- **Issue:** Hardcoded empty `OPENROUTER_API_KEY=""` at top of `app.py` (dead code, actual loading in `Ai_Chat`).

### 3. Documentation & Deliverables (20/25)
- `milestone2_demo_script.md` present but thin — 3 scenarios with confusing/contradictory expected vs failure columns. Needs significant improvement.
- `MVP_test_cases.md` present with 10 test cases, all marked passing — contradicts the 6/20 failures in evaluation. Seems optimistic.
- `MVP_known_issues.md` present — lists ingredient matching, UI, and data quality issues. ✓
- `MVP_retrospective.md` present — covers what changed, cut from scope, needs work. ✓
- PRD.md updated. ✓
- README.md with installation, CLI/GUI usage, file tree, screenshots. ✓
- Demo video links present. ✓
- `evaluation_test_cases.md` with 20 test cases and metrics (80% feasibility pass, 5% invented ingredient rate). ✓
- **MISSING:** `.env.example` — explicitly listed as a "must fix before Milestone 2" item and still not present.
- Missing metrics: expiry utilization rate and validator rejection rate not reported.

### 4. Evaluation Evidence (14/15)
- 20 evaluation test cases with screenshots and pass/fail results.
- Metrics: 80% feasibility pass rate, 5% invented ingredient rate, 1.05 avg regeneration attempts.
- Honest reporting of 6 failures with identified root causes (unit conversion).
- MVP test cases (10) are less convincing — all marked passing despite known issues.

### 5. Repository Hygiene (13/15)
- `.gitignore` present and covers .env, pycache, venvs.
- `requirements.txt` present (in both root and src/).
- README comprehensive with screenshots.
- SQLite database with proper schema.
- **Missing:** `.env.example`.
- **Issue:** `docs/` folder in `.gitignore` but docs are still tracked — contradictory.

---

## Individual Grades

| Team Member | Commits | Contribution Area | Grade |
|---|---|---|---|
| Luis M (OrangeXR) | 143 | Backend (Flask app, OpenRouter integration, inventory, README, chatbox) — primary engineer | 95/100 |
| Abigail Rodriguez Vazquez | 138 | Evaluation test cases, CSS, chat window, validation rules, docs | 92/100 |
| Jaylynn Vega | 21 | Documentation (retrospective, known issues, demo script, PRD updates) | 82/100 |
| Taja Hicks (AlexandriaTH) | 18 | Evaluation test cases, screenshots, category ordering | 80/100 |
| Emma Whitehead (nerevar) | 10 | Ingredient matching in validator, system prompt, known issues | 78/100 |

**Note:** Luis and Abigail carried the bulk of the work. Jay, Taja, and Emma had lighter contributions — particularly Emma with only 10 commits. All three need to increase their code contributions for the final sprint.

---

## Key Recommendations for Sprint 2
✅1. Create `.env.example` immediately — this was a "must fix" item that's still missing.
2. Fix unit conversion failures (the 6/20 failing test cases).
3. Improve demo script with clear, non-contradictory scenarios.
4. Fix `sort_inventory()` to filter by player_id.
✅5. Consolidate generation logic — either populate `generator.py` or remove it.
✅6. Remove hardcoded empty API key from `app.py`.
7. Report missing metrics (expiry utilization rate, validator rejection rate).
8. Emma, Taja, and Jay need to take on more coding tasks.
