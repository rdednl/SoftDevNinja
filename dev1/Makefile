all:
	ls pictures/*.jpg
	for pic in pictures/*.jpg; \
	do \
		pic_name=$$(stat -c %n  "$$pic" | sed 's-.*/--') ; \
		pic_lastmod=$$(stat -c %Y "$$pic") ; \
		thumb_lastmod=$$(stat -c %Y thumbs/$$pic_name 2>/dev/null) ; \
		if [ -z "$$thumb_lastmod" ]; then thumb_lastmod=0; fi ; \
		if [ $$thumb_lastmod -lt $$pic_lastmod ] ; \
		then \
			convert -thumbnail 100 pictures/$$pic_name thumbs/$$pic_name ; \
		fi; \
	done
