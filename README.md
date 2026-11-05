# Analysis of Patient Reviews on Hospitals and Healthcare Providers

## Overview
Topic modeling and sentiment analysis of ~30,000 patient reviews across 1,904 medical providers, using the Yelp Open Dataset. The goal is to identify which aspects of the patient experience drive satisfaction — information that a star rating alone cannot provide.

## Motivation

Hospitals collect patient feedback through standardized surveys, but those surveys ask a fixed set of questions, so patients can only respond to what they are asked. Online reviews work the other way around: patients write them unprompted and choose what to talk about. That makes them a useful place to look for service gaps a survey might not capture.

## Objectives
Two questions drive the analysis:

1. What recurring themes emerge from patient reviews?
2. Which aspects of patient experience are most strongly associated with overall satisfaction?

## Data

| Source | Yelp Open Dataset ([link](https://business.yelp.com/data/resources/open-dataset/)) |
|---|---|
| Business records | 150,346 → 11,890 after filtering to medical categories |
| Reviews | ~6.9M → 196,580 after joining on medical business IDs |
| Final dataset | 29,754 reviews across 1,904 providers |

Non-medical and adjacent categories (veterinary, cosmetic, dental, optical) were excluded during filtering.

## Methods

**Topic modeling** — Reviews were converted to TF-IDF vectors, then factorized with NMF into eight topics. Each review was assigned to its highest-weighted topic. Topics were labeled by inspecting their top terms.

**Sentiment analysis** — VADER, a lexicon-and-rule-based scorer, assigned each review a compound score from −1 to +1.

Stack: `pandas`, `scikit-learn`, `vaderSentiment`, `matplotlib`

## Key Findings

### 1. Reviews are polarized; provider averages are not

40.2% of reviews are 1-star and 42.2% are 5-star, producing a U-shaped distribution — patients write when an experience is exceptional or infuriating, rarely when it is merely adequate. Provider averages, by contrast, cluster toward the middle, since the extremes cancel out at the business level.

### 2. Rating declines steadily with review length

| Words per review | Mean stars |
|---|---|
| 0–50 | 3.59 |
| 50–100 | 3.36 |
| 100–150 | 2.93 |
| 150–200 | 2.66 |
| 200–250 | 2.42 |
| 250–300 | 2.38 |
| 300+ | 2.09 |

A purely structural feature — no content analysis required — that reflects how patients document care. Complaints require explaining what happened and who was involved; satisfaction needs a few sentences.

### 3. Dissatisfaction is operational, not clinical

| Theme | Reviews | Mean stars | % of corpus |
|---|---|---|---|
| Positive staff experience | 3,798 | 4.67 | 12.8 |
| Continuity of care | 5,426 | 4.08 | 18.2 |
| Urgent and primary care settings | 2,495 | 3.57 | 8.4 |
| Surgical and rehabilitation care | 2,062 | 3.43 | 6.9 |
| Hospitals and emergency care | 3,649 | 2.80 | 12.3 |
| Administrative staff interactions | 3,316 | 2.24 | 11.1 |
| Waiting and appointment delays | 4,220 | 2.23 | 14.2 |
| Disputed interactions | 4,788 | 1.57 | 16.1 |

The three lowest-rated themes are all operational and together account for ~41% of reviews. Clinical themes rank considerably higher. Staff interaction appears at both extremes of the ranking, suggesting interpersonal treatment is something patients notice sharply in both directions.

### 4. VADER under-detects negativity

Sentiment scores reproduce the same bimodal shape as the star ratings, but the peaks are lopsided — roughly four times as many reviews at the positive extreme as the negative one, despite the ratings being nearly symmetric. Satisfaction is voiced in evaluative vocabulary the lexicon contains ("great", "helpful"); dissatisfaction is described through events — a long wait, an unreturned call, an unexpected bill — that carry little negative vocabulary.

This is a limitation of lexicon-based scoring, but it is also a finding about how patients articulate dissatisfaction in healthcare settings.

## Recommendations

- **Read the longest reviews first.** Rating declines steadily with length, and long reviews contain the detail needed to diagnose what went wrong.
- **Prioritize administrative and front-desk operations.** The three lowest-rated themes are all operational; effort there is likely to move satisfaction more than equivalent effort on clinical service, which already rates higher.
- **Treat communication failures as most urgent.** "Disputed interactions" is the lowest-rated theme at 1.57 stars, and its top terms (told, said, insurance, called, asked) point to misunderstandings about coverage and follow-up rather than dissatisfaction with treatment.

## Future work

**Aspect-based sentiment analysis** would score sentiment at the clause level, letting a single review register approval of clinical staff alongside criticism of billing rather than collapsing to one label. Attempted here but dropped due to memory constraints.

**Temporal analysis** using review timestamps would show whether themes shift over time and whether providers exhibit sustained trends rather than static averages.

## References

Hutto, C. J., & Gilbert, E. (2014). VADER: A parsimonious rule-based model for sentiment analysis of social media text. *Proceedings of the Eighth International AAAI Conference on Weblogs and Social Media.*

Lee, D. D., & Seung, H. S. (1999). Learning the parts of objects by non-negative matrix factorization. *Nature, 401*(6755), 788–791.

Pedregosa, F., et al. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research, 12*, 2825–2830.

Spärck Jones, K. (1972). A statistical interpretation of term specificity and its application in retrieval. *Journal of Documentation, 28*(1), 11–21.

## Note on AI assistance

Claude was used for code review and debugging, for developing understanding of TF-IDF, NMF, and VADER, and for feedback on the written report. All analytical decisions, interpretation, and conclusions are my own.
