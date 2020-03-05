# Python-basics



# If your company has recently moved to using a new domain, but a lot of the company email addresses are still using the old one. You can replace the old domain with the new one in any outdated email addresses. 
# The function to replace the domain would look like this:

- def replace_domain(email, old_domain, new_domain):
  - if "@" + old_domain in email:
    - index = email.index("@" + old_domain)
    - new_email = email[:index] + "@" + new_domain
    - return new_email
  - return email


= old_domain IN email - True or False (if TRUE that the @ sign and old domain are contained in the email address)
= index = email.index("@" + old_domain).  - find out the old domain and where the @ sign starts
= email[:index] = based on the above findings create the new email

= last line "return email" is if the True or False check (if "@" + old_domain in email:) was FALSE
