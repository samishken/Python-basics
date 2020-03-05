# Python-basics



# If your company has recently moved to using a new domain, 
# but a lot of the company email addresses are still using the old one. 
# You can replaces the old domain with the new one in any outdated email addresses. 
# The function to replace the domain would look like this:

def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
    index = email.index("@" + old_domain)
    new_email = email[:index] + "@" + new_domain
    return new_email
  return email
