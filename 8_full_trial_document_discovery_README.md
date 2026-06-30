# Full Trial Document Discovery Notebook

`8_full_trial_document_discovery.ipynb` is a notebook-first, pandas-based discovery workflow for MindReader Biotech. It searches public evidence for a clinical asset, drug, or trial across registries, literature metadata, open full text, chemical databases, web/OSINT results, and PDFs.

It is designed for oncology and autoimmune assets, and uses BEN-2293 / BenevolentAI / atopic dermatitis as the default example.

## Required packages

- `requests`
- `pandas`
- `numpy`

The notebook also uses Python standard-library modules: `os`, `re`, `json`, `time`, `textwrap`, `datetime`, `urllib.parse`, `xml.etree.ElementTree`, `pathlib`, and `hashlib`.

## Optional packages

- `beautifulsoup4` for cleaner webpage text extraction
- `PyMuPDF` (`fitz`) for PDF text extraction
- `tqdm` for progress bars

## Optional API keys

Set these environment variables before running the notebook:

- `EXA_API_KEY`: enables Exa REST web discovery when `USE_EXA=True`
- `SEMANTIC_SCHOLAR_API_KEY`: improves Semantic Scholar rate limits
- `NCBI_API_KEY`: improves NCBI/PubMed rate limits
- `NCBI_EMAIL`: sent with NCBI/OpenAlex requests when available

If a key is missing, the notebook skips or rate-limits that source gracefully.

## Source limitations

We retrieve all discoverable public, open-access, and user-provided documents from configured sources. Paywalled, private, unpublished, removed, or inaccessible material may not be retrievable.

PubMed is not enough by itself because it mainly catches title, abstract, and metadata. It may miss mentions that appear only in body text, tables, figure captions, supplementary files, PDFs, company pages, conference pages, investor decks, or registry result pages.

The notebook does not bypass paywalls and stores short snippets only, not full copyrighted article or PDF bodies.

## Output files

The notebook writes outputs under `discovery_outputs/`:

- `aliases.csv`
- `query_bank.csv`
- `ctgov_trials.csv`
- `pubmed_hits.csv`
- `pmc_fulltext_hits.csv`
- `europe_pmc_hits.csv`
- `chembl_aliases.csv`
- `crossref_hits.csv`
- `openalex_hits.csv`
- `semantic_scholar_hits.csv`
- `exa_web_hits.csv`
- `pdf_body_hits.csv`
- `deduped_document_hits.csv`
- `missed_by_pubmed.csv`
- `source_coverage.csv`
- `asset_dossier.json`

## Run it for BEN-2293

Open `8_full_trial_document_discovery.ipynb` and run top-to-bottom with the default input cell:

```python
ASSET_NAME = "BEN-2293"
SPONSOR = "BenevolentAI"
DISEASE = "atopic dermatitis"
NCT_IDS = []
TARGETS = ["TrkA", "pan-Trk", "neurotrophin"]
KNOWN_PMIDS = []
KNOWN_DOIS = []
KNOWN_URLS = []
```

For BEN-2293, the notebook is expected to show why PubMed may find only a small number of article hits, while registry, full-text, PDF, and web discovery can find additional public evidence such as ClinicalTrials.gov records and trial-result pages.

## Run it for an oncology asset

Change the input cell, for example:

```python
ASSET_NAME = "EXAMPLE-101"
SPONSOR = "Example Oncology Inc"
DISEASE = "non-small cell lung cancer"
NCT_IDS = ["NCT00000000"]
TARGETS = ["EGFR", "tyrosine kinase inhibitor"]
KNOWN_PMIDS = []
KNOWN_DOIS = []
KNOWN_URLS = []
COMPANY_DOMAIN = "exampleoncology.com"
```

Keep the conference query section enabled. The query bank includes oncology-oriented societies such as ASCO, ESMO, AACR, SITC, EHA, and ASH, plus SEC and company-site searches.

## Run it for an autoimmune asset

Change the input cell, for example:

```python
ASSET_NAME = "EXAMPLE-202"
SPONSOR = "Example Immunology Ltd"
DISEASE = "rheumatoid arthritis"
NCT_IDS = []
TARGETS = ["JAK1", "cytokine signaling"]
KNOWN_PMIDS = []
KNOWN_DOIS = []
KNOWN_URLS = []
COMPANY_DOMAIN = "exampleimmunology.com"
```

The query bank includes autoimmune and inflammatory disease sources such as ACR, EULAR, EADV, DDW, UEG, ADA, and ENDO.

## Notes

- No backend is built.
- No Pydantic, FastAPI, or database is used.
- Every source is tracked in the final source audit as searched or skipped with a reason.
- Every conclusion in the generated dossier should be traceable to source rows.
