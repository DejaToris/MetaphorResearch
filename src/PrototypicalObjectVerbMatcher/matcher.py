import argparse


def get_cli_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("verb", type=str, help="The target verb.")
    default_number_of_objects = 10
    parser.add_argument(
        "-n", "--number_of_objects_to_return", type=int, default=default_number_of_objects,
        help="Number of prototypical objects to match to the verb and return in the final list. "
             "Defaults to {0}.".format(default_number_of_objects))
    return parser.parse_args()


def get_prototypical_objects_for(verb, number_of_objects):
    return [verb] * number_of_objects


def main():
    args = get_cli_arguments()
    prototypical_objects = get_prototypical_objects_for(args.verb, args.number_of_objects_to_return)
    print(prototypical_objects)


if __name__ == '__main__':
    main()
