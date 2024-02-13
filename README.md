# ffuflist3r
This script will execute Sublist3r to enumerate subdomains and then use FFuF to perform fuzzing on each subdomain.

In this script:

run_sublist3r function takes a domain as input and runs Sublist3r to enumerate subdomains.
run_ffuf function takes the domain and the list of subdomains as input and runs FFuF to perform fuzzing on each subdomain.
main function orchestrates the execution of Sublist3r and FFuF.
The script assumes you have a wordlist.txt file containing a list of common fuzzing payloads.
You'll need to replace 'example.com' with your target domain, and ensure that you have the necessary wordlists and that Sublist3r and FFuF are properly installed and accessible in your environment. Additionally, customize the wordlists and adjust the script according to your specific use case.





