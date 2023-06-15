<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html"/>

  <xsl:template match="/">
    <html>
      <head>
        <link rel="stylesheet" type="text/css" href="/static/stylesheet.css"/>
      </head>
      <body>
        <xsl:copy-of select="."/>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
