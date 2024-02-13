import subprocess

def run_sublist3r(domain):
    try:
        sublist3r_process = subprocess.Popen(['sublist3r', '-d', domain], stdout=subprocess.PIPE)
        sublist3r_output, _ = sublist3r_process.communicate()
        subdomains = sublist3r_output.decode('utf-8').split('\n')

        return subdomains
    except Exception as e:
        print(f"Error running Sublist3r: {e}")
        return []

def run_ffuf(domain, subdomains):
    try:
        for subdomain in subdomains:
            if subdomain:
                ffuf_process = subprocess.Popen(['ffuf', '-w', 'wordlist.txt', '-u', f'http://{subdomain}.{domain}'], stdout=subprocess.PIPE)
                ffuf_output, _ = ffuf_process.communicate()
                print(ffuf_output.decode('utf-8'))
    except Exception as e:
        print(f"Error running FFuF: {e}")

def main():
    domain = 'example.com'

    subdomains = run_sublist3r(domain)
    if subdomains:
        run_ffuf(domain, subdomains)
    else:
        print("Sublist3r did not find any subdomains.")

if __name__ == "__main__":
    main()
