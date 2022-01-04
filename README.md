# Get-Public-IP
Get your public IP address emailed to you, usual for when you'll at home/work and your don't either have a static IP or a dynamic DNS.

This small python scripts logs into an email account, downloads any unread emails (marking them as read at the same time) and checks to see if any are from your allowed emails list.  Any emails that are, it replies back with your public IP address.  Lastly it deletes the email you sent, and any emails in the sent folder, that were sent to an allowed email address.

This works best if you set up an indepentent email, that just this program logs into, otherwise you could end up having emails deleted.  I also don't know how securely the passwords are transmitted over the internet, when logging into the server.

NOTE: The login password to your email server is left completely unencrypted within the script.

To get the script working:
  1.  pip install imap_tools, smtplib, ssl (might be others as well, see list of libraries)
  2.  Set the variables on lines 32 to 36
  3.  Line 36, is the list of email address that you want the program to reply to.  Emails from anybody else will be ignored.
  4.  Line 47 (optional) you can change the Subject and Body of the text here, of the email the script sends back to you.
  5.  Set up a Scheduled Task to automatically run the script every so often.



THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
