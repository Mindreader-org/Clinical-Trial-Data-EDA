# Trial Intelligence Card: NCT02057250


### Clinical & Pipeline Significance Scores

| View | Score |
|---|---|
| Balanced | 49.76/100 |
| Investor | 60.43/100 |
| Patient | 43.1/100 |
| Clinical Research | 51.6/100 |
| Regulatory | 51.26/100 |
| Data Confidence | 100.0/100 |


## Dimension-Level AI Analysis

### Trial Identity

**Summary:** AI analysis failed: Expecting value: line 1 column 1 (char 0)

**Positive signals:** Not available in source data.

**Risk signals:** Expecting value: line 1 column 1 (char 0)

**Missing evidence:** Not available in source data.

**Confidence:** low | **Interpretation:** insufficient

**Do not conclude:** Do not use this failed AI output for interpretation.

### Clinical Efficacy Interpretability

**Summary:** The trial is a Phase 3 completed usability study comparing sarilumab auto-injector to prefilled syringe, with a primary endpoint of device technical failures and a secondary endpoint of sarilumab exposure (AUC). No clinical efficacy endpoints (e.g., ACR scores, disease activity measures) are listed. Although results are posted, the available data pertain to device performance and pharmacokinetics, not therapeutic benefit. Therefore, efficacy cannot be interpreted from this source.

**Positive signals:** Study completed and results posted (has_results: true, raw_results_available: true); Phase 3 randomized parallel design with 217 enrolled patients

**Risk signals:** Primary endpoint measures device technical failure, not clinical efficacy; Secondary endpoint measures pharmacokinetic exposure (AUC), not a clinical outcome; Study is open-label (masking: NONE), raising potential bias; No placebo or active comparator arm for efficacy assessment; Enrollment per arm may be limited (~54 patients across 4 arms)

**Missing evidence:** Clinical efficacy endpoints such as ACR20/50/70, DAS28, or SDAI scores; Actual numerical results for primary and secondary outcomes; Comparative efficacy data versus control or standard therapy; Long-term outcome data beyond 12 weeks

**Confidence:** high | **Interpretation:** insufficient

**Do not conclude:** That sarilumab improves rheumatoid arthritis symptoms; That the auto-injector device confers clinical benefit over prefilled syringe; That the trial demonstrates therapeutic efficacy of sarilumab; That the observed PK exposure translates to clinical effect

### Endpoint Meaningfulness

**Summary:** The primary endpoint is the number of validated auto‑injector device (AID) associated product technical failures (PTFs) recorded from baseline to week 12, which assesses device usability rather than clinical efficacy or safety. This is a device‑performance endpoint, not a hard clinical outcome, patient‑reported outcome, surrogate disease marker, or safety measure. The secondary endpoint measures pharmacokinetic exposure (AUC) of sarilumab, a biomarker of drug concentration, not a clinical efficacy outcome. Thus, the endpoints focus on device reliability and drug PK rather than patient‑centered clinical benefit in rheumatoid arthritis.

**Positive signals:** Primary endpoint directly quantifies device technical failures, providing clear, objective data on usability.

**Risk signals:** Endpoints do not capture clinical efficacy, disease activity, or patient‑reported outcomes, limiting relevance to treatment benefit.; The primary endpoint is a device‑specific measure, which may not be meaningful to patients or clinicians focused on disease control.

**Missing evidence:** Clinical efficacy endpoints such as ACR response or DAS28 scores.; Patient‑reported outcome measures (e.g., pain, function).; Safety endpoints beyond device technical failures.

**Confidence:** high | **Interpretation:** moderate

**Do not conclude:** That the device is effective for treating rheumatoid arthritis.; That sarilumab improves clinical outcomes in RA.; That the trial demonstrated safety or efficacy of the drug.

### Safety and Tolerability

**Summary:** AI analysis failed: Error code: 429 - {'error': {'message': 'Rate limit exceeded: free-models-per-min. ', 'code': 429, 'metadata': {'headers': {'X-RateLimit-Limit': '16', 'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset'

**Positive signals:** Not available in source data.

**Risk signals:** Error code: 429 - {'error': {'message': 'Rate limit exceeded: free-models-per-min. ', 'code': 429, 'metadata': {'headers': {'X-RateLimit-Limit': '16', 'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': '1782152460000'}, 'provider_name': None, 'previous_errors': [{'code': 429, 'message': 'Rate limit 

**Missing evidence:** Not available in source data.

**Confidence:** low | **Interpretation:** insufficient

**Do not conclude:** Do not use this failed AI output for interpretation.

### Patient Adoption Burden

**Summary:** The study evaluated a sarilumab auto‑injector device (AID) versus a pre‑filled syringe in rheumatoid arthritis patients who were required to be willing and able to self‑inject. Participants recorded injection steps in a diary, and technical failures of the device were tracked over 12 weeks, indicating a focus on patient‑handled administration. The trial design required multiple clinic visits for pharmacokinetic sampling, suggesting some monitoring burden. Overall, the therapy is delivered via a self‑injectable device, but the source does not describe home‑use logistics or training specifics.

**Positive signals:** Eligibility required participants to be willing and able to self‑inject, indicating that the device is intended for patient‑managed administration.; Primary outcome measured patient ability to complete the injection steps, showing that usability was a central focus.

**Risk signals:** Requirement for participants to complete a diary and report technical complaints suggests potential complexity or burden in daily use.; Multiple scheduled PK blood draws imply clinic visit requirements that add to patient burden.

**Missing evidence:** Details on training required for correct self‑injection.; Confirmation of whether injections are performed at home or in a clinical setting.; Frequency of dosing and any required storage conditions.; Patient‑reported outcomes on ease of use beyond technical failure counts.

**Confidence:** high | **Interpretation:** weak

**Do not conclude:** Home use is possible or not.; Exact dosing frequency or schedule.; Cost or reimbursement implications.; Overall safety or efficacy of sarilumab.

### Study Design Quality

**Summary:** The trial is a Phase 3, multicenter, randomized, open‑label, parallel‑group interventional study with four arms and 217 participants evaluating the usability of a sarilumab auto‑injector versus a pre‑filled syringe. Randomization and a comparator device are present, but masking is absent and the primary endpoint focuses on technical failures rather than clinical efficacy. Enrollment is moderate, and the study duration (baseline to week 12) is short for assessing longer‑term outcomes.

**Positive signals:** Randomized allocation (design.allocation); Four parallel arms (design.number_of_arms); Multicenter enrollment across 53 sites in 6 countries (locations.facility_count, locations.countries); Adequate sample size for a usability endpoint (design.enrollment_count = 217)

**Risk signals:** Open‑label design with no masking (design.masking = NONE); Comparator is another device, not a placebo or active drug control, limiting efficacy interpretation; Primary outcome limited to device technical failures, not clinical efficacy or safety; Short follow‑up period (baseline to week 12) for a chronic disease

**Missing evidence:** Detailed allocation ratios and numbers per arm; Statistical power or sample‑size justification for the primary usability endpoint; Longer‑term clinical efficacy or safety outcomes; Rationale for lack of blinding

**Confidence:** high | **Interpretation:** moderate

**Do not conclude:** Efficacy of sarilumab for rheumatoid arthritis; Safety superiority of the auto‑injector device; Long‑term clinical benefit of the intervention; Definitive superiority of one delivery method over the other

### Regulatory Readiness

**Summary:** The study is a Phase 3, randomized, open‑label usability trial completed in 2016 with 217 participants. Its primary endpoint assesses technical failures of the auto‑injector device, not clinical efficacy or safety of sarilumab. Results are available, but the design and endpoints focus on device performance rather than regulatory‑grade efficacy or safety data, limiting its ability to support a pivotal regulatory filing.

**Positive signals:** Phase 3 designation; Randomized parallel‑group design; Study completed and results are available

**Risk signals:** Primary endpoint is a device usability metric, not a clinical efficacy or safety outcome; No masking (open‑label) and no efficacy endpoints; Enrollment of 217 may be insufficient for definitive efficacy assessment

**Missing evidence:** Clinical efficacy outcomes (e.g., ACR response, DAS28); Comprehensive safety data; Comparative effectiveness versus standard of care; Blinded assessment to reduce bias

**Confidence:** high | **Interpretation:** weak

**Do not conclude:** The trial is pivotal or sufficient for regulatory approval; Efficacy or safety of sarilumab has been demonstrated by this study; The auto‑injector device has received regulatory clearance based on this data

### Economic and Access Relevance

**Summary:** The trial compares a sarilumab auto‑injector device (AID) with a pre‑filled syringe (PFS) in rheumatoid arthritis patients, focusing on technical failures and pharmacokinetics rather than cost. The intervention is a biologic administered subcutaneously, implying a potentially high‑cost product and a delivery device that may affect access. The multicenter, international setting across 53 sites suggests broad geographic reach but does not address reimbursement or pricing mechanisms. No economic, pricing, or reimbursement data are reported in the source.

**Positive signals:** Inclusion of a device (auto‑injector) allows assessment of usability, which can influence patient adherence and indirect cost considerations.

**Risk signals:** Absence of any cost, pricing, or reimbursement information limits assessment of economic impact.; The study design focuses on technical failures, not on health‑economic outcomes such as cost‑effectiveness or budget impact.

**Missing evidence:** Pricing or list price of sarilumab and the auto‑injector versus pre‑filled syringe.; Reimbursement status or payer coverage policies in the trial countries.; Health‑economic endpoints (e.g., cost per responder, resource utilization).; Comparative cost analysis of device versus syringe administration.

**Confidence:** high | **Interpretation:** weak

**Do not conclude:** The actual price of sarilumab or the auto‑injector.; Whether the device is reimbursed or covered by insurers.; Cost‑effectiveness or budget impact of the device versus syringe.; Any conclusions about overall affordability for patients or health systems.

### Evidence Transparency

**Summary:** The trial is marked as COMPLETED with results posted and raw results available, but no linked publications are provided. Primary and secondary endpoints are clearly described in the source data. While outcome data exist, the lack of peer‑reviewed publication limits external validation.

**Positive signals:** has_results is true and raw_results_available is true, indicating that outcome data have been posted; primary and secondary endpoint measures are explicitly listed

**Risk signals:** publication_count is 0 and publications list is empty, so no peer‑reviewed source is available; absence of detailed result tables or summary metrics in the source data

**Missing evidence:** linked journal article or conference abstract summarizing the results; detailed numerical results for the primary and secondary endpoints

**Confidence:** high | **Interpretation:** moderate

**Do not conclude:** Efficacy or safety conclusions without seeing the actual result data; Regulatory approval status based on this trial alone; Market or commercial implications

### Red-Team Risk Review

**Summary:** The trial is a completed Phase 3, randomized, open‑label usability study comparing a sarilumab auto‑injector device with a pre‑filled syringe in 217 rheumatoid arthritis patients. The primary endpoint focuses on device‑related technical failures rather than clinical efficacy or safety. While the study design includes randomization and a sizable multinational enrollment, the lack of masking and the narrow outcome scope limit the ability to infer therapeutic benefit or risk.

**Positive signals:** Randomized parallel‑group design with 217 participants across 53 sites in multiple countries; Completion of a Phase 3 study with primary data on device technical failures

**Risk signals:** Open‑label (no masking) design introduces potential bias in reporting device failures; Primary outcome measures only device usability, not clinical efficacy or safety of sarilumab; No published results or detailed statistical data are provided in the source

**Missing evidence:** Efficacy outcomes for sarilumab (e.g., disease activity scores); Safety/adverse event data for the drug and device; Statistical analysis of the primary endpoint (failure rates, confidence intervals); Comparative effectiveness between auto‑injector and pre‑filled syringe

**Confidence:** high | **Interpretation:** moderate

**Do not conclude:** That sarilumab is clinically effective or safe based on this trial; That the auto‑injector device improves patient outcomes beyond usability; Any market, regulatory, or investment implications; Comparative superiority of the auto‑injector over the pre‑filled syringe in disease control

### Population Relevance

**Summary:** The trial enrolled adults (≥18 years) with moderate-to-severe active rheumatoid arthritis who were candidates for anti‑IL‑6R therapy and able to self‑inject. Eligibility required continuous use of non‑biologic DMARDs and excluded prior exposure to IL‑6/IL‑6R antagonists, TNF antagonists, other biologics, and Janus kinase inhibitors. No upper age limit or sex restriction was specified, and the population is therefore relatively narrow, focusing on treatment‑naïve biologic‑eligible RA patients.

**Positive signals:** Clear inclusion criteria defining adult patients with moderate‑to‑severe RA and ability to self‑inject; Explicit exclusion of prior IL‑6/IL‑6R, TNF, and other biologic therapies, creating a well‑characterized cohort

**Risk signals:** Population is narrow due to multiple prior‑treatment exclusions, limiting applicability to broader RA populations; No maximum age specified, but lack of age stratification creates uncertainty about older adult representation

**Missing evidence:** Upper age limit or age distribution of enrolled participants; Details on disease severity metrics (e.g., DAS28 scores) used to define 'moderate‑to‑severe'; Information on sex distribution and other demographic characteristics

**Confidence:** high | **Interpretation:** moderate

**Do not conclude:** Generalizability to pediatric patients or to RA patients with prior biologic exposure; Efficacy or safety outcomes for the broader RA population; Real‑world applicability beyond the defined eligibility criteria
