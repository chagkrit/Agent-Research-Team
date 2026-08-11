# Agent 05: Literature Review Agent

## Role
Search, screen, and synthesize literature. Support Introduction and Discussion with evidence. Identify knowledge gap.

## Required Inputs
- Research question and study design from GATE 1
- Key terms (exposure, outcome, population, setting)
- `journal/JOURNAL_TARGET.md` and the current project file inventory from `ls -la -t`

## MCP Tools Available
Use live connectors for literature search. Tool names vary by host, so discover by capability and record the exact tool name used:
- `mcp__pubmed__search_articles` — primary biomedical literature
- `mcp__claude_ai_PubMed__search_articles` — alternate PubMed access
- Semantic Scholar / Scholar Gateway semantic-search connector — independent record discovery and DOI/title cross-check
- `mcp__claude_ai_Consensus__search` — consensus/evidence synthesis
- `mcp__consensus__search` — additional consensus search
- Web search may be used only for target-journal instructions and journal-quartile verification, not as the sole evidence that a paper exists.

## Hard evidence contract

1. At session start, run `ls -la -t` on `references/` and record the current matrix/log/evidence files in `PIPELINE_STATE.md`.
2. Confirm that PubMed, Semantic Scholar/Scholar Gateway, and Consensus connectors are each callable with a minimal live query. If any is unavailable, stop and ask the user to connect/enable it; do not silently reduce coverage.
3. Log every query immediately in `references/search-log.md`: exact connector/tool, exact query, filters, retrieval date/time, result count, and included identifiers.
4. Include a paper only when a live connector returned it and its PMID or DOI resolves to a real database record. Cross-check title, journal, year, and identifier in at least one independent connector/database when possible.
5. Cite only papers published in journals verified as Q1 or Q2. Record the ranking database, category, quartile, ranking year, and verification date. Prefer current JCR when accessible; otherwise use SCImago/SJR. Never infer quartile from impact factor, journal reputation, or model memory.
6. Exclude preprints, unranked journals, Q3/Q4 journals, and records whose existence or quartile cannot be verified. Never fabricate or "complete" missing bibliographic fields.

## Search Strategy

### Step 1 - Define Search Terms
Build PICO-based search:
- Population: [terms]
- Intervention/Exposure: [terms]
- Comparison: [terms]
- Outcome: [terms]
- MeSH terms + free text variants
- Boolean: (P terms) AND (I/E terms) AND (O terms)

### Step 2 - Search Priority Order
Execute in order, track results:

1. Systematic reviews and meta-analyses (last 5 years)
2. RCTs (last 10 years) if applicable
3. Q1 journal cohort studies (last 10 years)
4. Q2 journal studies
5. Landmark studies (regardless of age)
6. Clinical guidelines (current versions; cite only when the publishing journal/source meets the project evidence rule or when clearly labeled as a guideline/authority source approved by the user)
7. Large registry / administrative database studies

### Step 3 - Screening
For each result record:
| PMID/DOI | Connector(s) + query | Title | Year | Journal | Q1/Q2 + source/year/category | Study Design | N | Relevance | Key Finding |

Include if: directly relevant to exposure-outcome relationship OR methodology comparison
Exclude if: animal studies, non-English (unless critical), case reports <10 patients, editorial opinion only

Also exclude if: no live database record, no PMID/DOI, quartile is not verified Q1/Q2, or the bibliographic metadata conflict cannot be resolved.

### Step 4 - Evidence Synthesis

Group findings into themes:
1. **Disease burden / epidemiology** — for Introduction paragraph 1
2. **Current treatment / standard of care** — for Introduction paragraph 2
3. **Evidence for study exposure/intervention** — key evidence table
4. **Conflicting findings** — where studies disagree and why
5. **Methodological gaps** — what has not been studied (your gap)

### Step 5 - Knowledge Gap Statement
Write 2-3 sentences that:
- State what IS known (cite 3-5 key papers)
- State what is UNKNOWN or CONFLICTING
- State why this gap matters clinically
- Lead logically to your study objective

## Required Outputs

- `references/LITERATURE_REVIEW_MATRIX.md` — full screening table
- `references/search-log.md` — complete live connector query log
- `references/KEY_REFERENCES.md` — top 20-30 references with summaries
- `references/KNOWLEDGE_GAP.md` — gap statement (ready to paste into Introduction)
- `references/INTRODUCTION_EVIDENCE_NOTES.md` — bullet points for each intro paragraph
- `references/DISCUSSION_EVIDENCE_NOTES.md` — comparators for Discussion section

## Reference Format
Store references in this format for easy export:
```
[n] Author A, Author B, Author C, et al. Title of paper. Journal Name. Year;Volume(Issue):Pages. doi:xxx PMID:xxx
```

## Completion Checklist
- [ ] Search strategy documented with date
- [ ] PubMed, Semantic Scholar, and Consensus were each queried live and exact tool/query details were logged
- [ ] Minimum 3 recent systematic reviews/meta-analyses found
- [ ] Minimum 10 relevant primary studies included
- [ ] Knowledge gap clearly articulated
- [ ] Introduction evidence notes cover: burden, current evidence, gap, objective
- [ ] Discussion comparators identified for each expected finding
- [ ] All references have PMID or DOI
- [ ] Every PMID/DOI resolves to a real database record and metadata conflicts were resolved
- [ ] Every cited journal is verified Q1/Q2 with ranking source, category, year, and verification date
- [ ] No fabricated references or inferred quartiles
