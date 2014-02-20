#include <stdio.h>

#include "config.h"
#include "version.h"

#ifdef SOUND
static char *
sound(void)
{
    return "enabled";
}
#else
static char *
sound(void)
{
    return "disabled";
}
#endif

#ifdef GUI
#include <gtk/gtk.h>

static void
gui(void)
{
    GtkWidget *dialog;

    gtk_init(NULL, NULL);
    dialog = gtk_message_dialog_new (NULL,
        GTK_DIALOG_DESTROY_WITH_PARENT,
        GTK_MESSAGE_INFO,
        GTK_BUTTONS_CLOSE,
        "GUI is enabled\nSound is %s", sound());
    gtk_dialog_run (GTK_DIALOG (dialog));
    gtk_widget_destroy (dialog);

    return;
}
#else
static void
gui(void)
{
    return;
}
#endif

int
main()
{
    printf("Hello from %s-%s\n", PROJECT_NAME, PROJECT_VERSION);
    gui();
    return 0;
}
