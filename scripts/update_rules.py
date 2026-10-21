import urllib.request
import yaml
import os
import sys

def main():
    sub_url = os.environ.get('SUB_URL')
    if not sub_url:
        sys.exit(1)

    req = urllib.request.Request(sub_url, headers={'User-Agent': 'ClashforWindows/0.20.39'})
    
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            content = response.read().decode('utf-8')
            
        config = yaml.safe_load(content)
        
        if 'rules' not in config:
            sys.exit(1)

        new_rules = config['rules']
        new_data = {"payload": new_rules}

        file_path = "acyun_rules.yaml"
        
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    existing_data = yaml.safe_load(f)
                
                if existing_data == new_data:
                    sys.exit(0)
            except Exception:
                pass

        with open(file_path, "w", encoding="utf-8") as f:
            yaml.dump(new_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

    except Exception:
        sys.exit(1)

if __name__ == "__main__":
    main()
