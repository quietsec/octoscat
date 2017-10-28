Octoscat
========

Octoscat is both a small library that can be used to detect high-entropy strings, and a cli tool that searches through git commit history for high-entropy strings (things like RSA keys, tokens, secrets, etc).


#### How does it work?

There is nothing fancy or magic about how octoscat works, it's rather simple. You feed it strings (git commit diffs, emails, or whatever your heart desires), and it will just iterate through each line, word, and character to find strings that look like they could be secrets.

Potential secrets are found by checking if each character of each word (space separated strings) contain characters allowed in the BASE64 and HEX character sets. If you happen to come across a string that is >20 characters, and each character lives within those two character sets -- it might be a secret!

Then using `shannon entropy`, octoscat calculates entropy of the potential secret strings. If the entropy is beyond a certain threshold, it is deemed a secret and returned as a positive match.

This approach is not bulletproof. You will likely run into many false positives, but it should find most of the real secrets. If you can think of a way to improve the accuracy, please feel free to open a pull request or discuss in the github issues.

#### Contributors

Thank you to all of the folks who have contributed to this project:

* quietsec
* Octoscat was heavily inspired by https://github.com/dxa4481/truffleHog
* [your name here]


#### TODO

* [ ] Add the ability to query all repos of a given github organization.
* [ ] Add the ability to query all organization members' public github repositories.
* [ ] Add the ability to store results in a way that can be rendered in a web interface.
* [ ] Add the ability to run this tool continuously, and get notified when new positive matches occur.
