from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import cgi

class NotFoundPageHandler(webapp.RequestHandler):
  def get(self):
    self.error(404)
    self.response.out.write("""<html><head>
<meta http-equiv="content-type" content="text/html;charset=utf-8">
<title>404 Not Found</title>
</head>
<body>
<p>The requested URL <code>%s</code> was not found on this server.</p>
<p>Sorry, I took down a lot of older content. Contact me at <a
href="mailto:russ@yanofsky.org">russ@yanofsky.org</a> if there's something I
should put back up, or anything I can help you with.</p>
</body></html>""" % cgi.escape(self.request.path))

application = webapp.WSGIApplication([('/.*', NotFoundPageHandler)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
