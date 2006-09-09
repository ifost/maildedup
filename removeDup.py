#!/usr/bin/python

# This program removes duplicated messages from a mailbox
import mailbox

fp = open('/var/spool/mail/gregb')
mb = mailbox.UnixMailbox(fp)

outfp = open('/tmp/mailbox-gregb','w')

prev = None
msg = mb.next()
while msg is not None:
   try:
     msgid = msg['Message-ID']
   except:
     msgid = None
   if (prev is not None) and (msgid is not None) and (prev == msgid):
      print "Skipping duplicate message",msgid
      msg = mb.next()
      continue
   msg.fp.seek(msg.startofheaders)
   outfp.write(msg.fp.read())
   print "Wrote",msgid
   msg = mb.next()
