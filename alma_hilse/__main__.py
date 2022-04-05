import typer
from alma_hilse.lib.lo_timing.lftrr import Lftrr

# from alma_hilse.lib.corr import drx
from alma_hilse import __version__
from typing import Optional

# Command-line application commands and subcommands based in Typer
app = typer.Typer(add_completion=False)
timing_app = typer.Typer(short_help="LFTRR/LORR related commands")
app.add_typer(timing_app, name="timing")
corr_app = typer.Typer(short_help="HILSE correlator related commands")
app.add_typer(corr_app, name="corr")


@app.callback()
def callback():
    """
    Collection of diagnostics and configuration commands for ALMA HILSE
    """


@corr_app.callback()
def corr_app_callback():
    """
    Obtain basic status of HILSE correlator device.

    Usage:

    \b
    alma-hilse corr xxxxx # XXXXXX

    """


@app.command(short_help="Show current version")
def version():
    print(__version__)


@timing_app.callback()
def timing_app_callback():
    """
    Obtain basic status of HILSE LFTRR device and issue resync command.

    Referring to the status, a stripped down version of the LORR status is presented,
    focusing only on variables relevant to HILSE.

    Usage:

    \b
    alma-hilse timing status # Display LFTRR status
    alma-hilse timing resync # Resync TE to central reference
    alma-hilse timing clear  # Clear TE and PLL error flags

    """


@timing_app.command("status", short_help="LFTRR healthcheck")
def status_lftrr(
    abm: Optional[str] = typer.Option(None, help="ABM name for AmbManager"),
    node: Optional[int] = typer.Option(None, help="Node id for LFTRR/LORR"),
    channel: Optional[int] = typer.Option(None, help="Channel number for LFTRR/LORR"),
):
    try:
        lftrr = Lftrr(abm, node, channel)
        lftrr.status()
    except Exception as e:
        print(f"Error: {str(e)}")


@timing_app.command("resync", short_help="Resync TE to central reference")
def resync_te():
    try:
        lftrr = Lftrr()
        lftrr.resync_te()
    except Exception as e:
        print(f"Error: {str(e)}")


@timing_app.command("clear", short_help="Clear TE and PLL error flags")
def clear_flags():
    try:
        lftrr = Lftrr()
        lftrr.clear_flags()
    except Exception as e:
        print(f"Error: {str(e)}")


@corr_app.command("status", short_help="DRX power and status check")
def status_drx():
    drx.get_drx_status()


def main():
    app()


if __name__ == "__main__":
    main()
