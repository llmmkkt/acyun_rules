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
        rules = config.get('rules', [])
        
        output_data = {"payload": rules}

        with open("acyun_rules.yaml", "w", encoding="utf-8") as f:
            yaml.dump(output_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

    except Exception:
        # 失败时也生成一个空规则，防止后续 git add 报错
        with open("acyun_rules.yaml", "w", encoding="utf-8") as f:
            yaml.dump({"payload": []}, f, allow_unicode=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
