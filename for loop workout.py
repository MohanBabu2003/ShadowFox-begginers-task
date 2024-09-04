def workout_routine():
    total_jumping_jacks = 100
    completed_jumping_jacks = 0
    set_size = 10

    while completed_jumping_jacks < total_jumping_jacks:
        # Perform a set of jumping jacks
        completed_jumping_jacks += set_size
        
        # Ask if the user is tired
        response = input(f"Completed {completed_jumping_jacks} jumping jacks. Are you tired? (yes/no): ").strip().lower()
        
        if response in ['yes', 'y']:
            # Ask if the user wants to skip the remaining sets
            skip_response = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()
            if skip_response in ['yes', 'y']:
                print(f"You completed a total of {completed_jumping_jacks} jumping jacks.")
                return
            else:
                # Continue workout and display remaining jumping jacks
                remaining_jumping_jacks = total_jumping_jacks - completed_jumping_jacks
                print(f"Remaining jumping jacks: {remaining_jumping_jacks}")
        else:
            # Continue workout and display remaining jumping jacks
            remaining_jumping_jacks = total_jumping_jacks - completed_jumping_jacks
            print(f"Remaining jumping jacks: {remaining_jumping_jacks}")
    
    # If completed all jumping jacks
    print("Congratulations! You completed the workout.")

# Run the workout routine
workout_routine()
