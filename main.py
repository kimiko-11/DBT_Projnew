from participant_login import participant_login
from examiner_login import examiner_login

def main():
    # Start with participant or examiner login
    choice = input("Enter 1 for Participant Login, 2 for Examiner Login: ")
    if choice == '1':
        participant_login()
    elif choice == '2':
        examiner_login()

if __name__ == "__main__":
    main()
