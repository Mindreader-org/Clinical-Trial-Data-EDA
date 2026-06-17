import urllib.request
import urllib.parse
import json
import csv
import time
import sys
import os

def fetch_category_trials(category, condition_query, target_count=3500):
    base_url = "https://clinicaltrials.gov/api/v2/studies"
    params = {
        "query.cond": condition_query,
        "pageSize": 1000,
        "countTotal": "true"
    }
    
    trials = []
    page_token = None
    fetched_count = 0
    total_count = None
    
    print(f"Starting fetch for category '{category}' with condition query '{condition_query}'...")
    
    while fetched_count < target_count:
        if page_token:
            params["pageToken"] = page_token
        else:
            params.pop("pageToken", None)
            
        url = base_url + "?" + urllib.parse.urlencode(params)
        print(f"Fetching page... ({fetched_count} retrieved so far)")
        
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode('utf-8'))
        except Exception as e:
            print(f"Error fetching data: {e}", file=sys.stderr)
            break
            
        if total_count is None:
            total_count = data.get("totalCount", 0)
            print(f"Total matching studies available in API: {total_count}")
            
        studies = data.get("studies", [])
        if not studies:
            print("No more studies returned by the API.")
            break
            
        for study in studies:
            protocol = study.get("protocolSection", {})
            id_module = protocol.get("identificationModule", {})
            status_module = protocol.get("statusModule", {})
            sponsor_module = protocol.get("sponsorCollaboratorsModule", {})
            design_module = protocol.get("designModule", {})
            conditions_module = protocol.get("conditionsModule", {})
            
            nct_id = id_module.get("nctId", "")
            brief_title = id_module.get("briefTitle", "")
            official_title = id_module.get("officialTitle", "")
            status = status_module.get("overallStatus", "")
            
            start_date = status_module.get("startDateStruct", {}).get("date", "")
            completion_date = status_module.get("completionDateStruct", {}).get("date", "")
            
            sponsor = sponsor_module.get("leadSponsor", {}).get("name", "")
            study_type = design_module.get("studyType", "")
            
            phases_list = design_module.get("phases", [])
            phase = phases_list[0] if phases_list else "NA"
            
            enrollment = design_module.get("enrollmentInfo", {}).get("count", 0)
            
            conditions_list = conditions_module.get("conditions", [])
            conditions = ", ".join(conditions_list)
            
            trial_row = {
                "nct_id": nct_id,
                "brief_title": brief_title,
                "official_title": official_title,
                "category": category,
                "status": status,
                "start_date": start_date,
                "completion_date": completion_date,
                "sponsor": sponsor,
                "study_type": study_type,
                "phase": phase,
                "enrollment": enrollment,
                "conditions": conditions
            }
            trials.append(trial_row)
            fetched_count += 1
            if fetched_count >= target_count:
                break
                
        page_token = data.get("nextPageToken")
        if not page_token:
            print("Reached the end of the query (no nextPageToken).")
            break
            
        # Respect API rate limits
        time.sleep(0.5)
        
    return trials

def main():
    # Set relative execution to the script's directory so it writes in dataset/
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Fetch Autoimmune (Autoimmune OR Diabetes OR Arthritis)
    auto_trials = fetch_category_trials("Autoimmune", "Autoimmune OR Diabetes OR Arthritis", target_count=3500)
    
    # Fetch Oncology (Oncology OR Cancer OR Leukemia OR Lymphoma OR Tumor)
    onc_trials = fetch_category_trials("Oncology", "Oncology OR Cancer OR Leukemia OR Lymphoma OR Tumor", target_count=3500)
    
    all_trials = auto_trials + onc_trials
    print(f"Total retrieved trials: {len(all_trials)}")
    
    csv_file = "clinical_trials.csv"
    headers = [
        "nct_id", "brief_title", "official_title", "category", "status",
        "start_date", "completion_date", "sponsor", "study_type", "phase",
        "enrollment", "conditions"
    ]
    
    with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in all_trials:
            writer.writerow(row)
            
    print(f"Successfully wrote {len(all_trials)} clinical trials to {csv_file}")

if __name__ == "__main__":
    main()
