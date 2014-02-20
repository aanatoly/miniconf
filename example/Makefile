## miniconf makefiles ## 1.1 ##

TOPDIR := ..

misc_src = misc.c
misc_type = lib

hello_src = hello.c
hello_cflags += $(if $(GUI),$$(GTK2_CFLAGS)) \
	$(if $(SOUND),$(ALSA_CFLAGS))
hello_libs += $(if $(GUI),$(GTK2_LIBS)) \
	$(if $(SOUND),$(ALSA_LIBS))
hello_type = bin

include $(TOPDIR)/.config/rules.mk
