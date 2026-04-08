import logging
from argparse import ArgumentParser, BooleanOptionalAction
from secrets import SystemRandom
from shutil import which
from subprocess import run

logger = logging.getLogger(__name__)


def generate_main_numbers(generator: SystemRandom, euro: bool) -> list[int]:
    max_number = 48 if not euro else 50
    select_numbers = 6 if not euro else 5
    result = generator.sample(list(range(1, max_number + 1)), select_numbers)
    result.sort()
    return result


def generate_bonus_numbers(generator: SystemRandom, euro: bool) -> list[int]:
    result = [generator.randint(1, 5)] if not euro else generator.sample(list(range(1, 12 + 1)), 2)
    result.sort()
    return result


def generate_text(main_numbers: list[int], bonus_numbers: list[int]) -> str:
    result = "Main numbers:\t" + " ".join(f"({n:02})" for n in main_numbers) + "\n\n"
    bonus_prefix = "Bonus number:\t" if len(bonus_numbers) == 1 else "Bonus numbers:\t"
    bonus_text = " ".join(f"({n:02})" for n in bonus_numbers)
    result += bonus_prefix + bonus_text
    return result


def print_log(text: str) -> None:
    text = text.replace("\n\n", "\n")
    logger.info(f"------------------------\n\n"
                f"{text}\n")


def show_cowsay(text: str) -> bool:
    if which("cowsay") is None:
        print("\nPlease install cowsay. Otherwise, please use --plain flag\n")
        return False

    print()
    run(["cowsay", "-W", "100", f"\n\n{text}\n\n"])
    print()
    print_log(text)
    return True


def show_plain(text: str) -> bool:
    text = text.replace("\n\n", "\n")
    print(f"\n{text}\n")
    print_log(text)
    return True


def show_text(plain: bool, text: str) -> bool:
    return show_plain(text) if plain else show_cowsay(text)


def setup_logging(log_file: str) -> None:
    logging.basicConfig(
            format="%(asctime)s %(message)s",
            level=logging.INFO,
            filename=log_file,
            filemode="a"
    )


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--plain", action=BooleanOptionalAction, help="print the result in plain mode")
    parser.add_argument("--euro", action=BooleanOptionalAction, help="generate numbers for Eurojackpot")
    parser.add_argument("--log", type=str, default="vikinglotto.log", help="path to log file")
    args = parser.parse_args()

    setup_logging(args.log)

    secret_generator = SystemRandom()
    main_numbers = generate_main_numbers(secret_generator, args.euro)
    bonus_numbers = generate_bonus_numbers(secret_generator, args.euro)
    text = generate_text(main_numbers, bonus_numbers)
    show_text(args.plain, text)


if __name__ == "__main__":
    main()
