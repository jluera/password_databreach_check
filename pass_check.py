import sys 
import requests
import hashlib 

def request_pwned_api_call(query_char):
    """ The actual API call """
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res

def get_pwned_pass_count(hashes, hashes_to_check):
    """ return the number of times the password has been listed in databreach records """
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for hash, count in hashes:
        if hash == hashes_to_check:
            return count
    return 0

def submit_pwned_pass_check(password):
    """ Submitting API call to pwnedpasswords to check if password has been leaked. """
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1pass[:5], sha1pass[5:]
    response = request_pwned_api_call(first5)
    return get_pwned_pass_count(response, tail)

def main(args):
    for password in args:
        count = submit_pwned_pass_checkk(password)
        if count:
            print(f'The password {password} was referenced in {count} databreaches according to pwnedpasswords.')
        else:
            print(f'The password {password} was NOT found in any databreach records.')
    return 'Check complete.'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
