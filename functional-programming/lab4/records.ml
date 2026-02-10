(* Madison Lovett, A01292253
   Feb 10, 2026 *)

(* This is a record *)
type record = { firstname : string; lastname : string; score : int }

(* This is a function that parses a line (string) that gets split on any number of whitespaces,
   it then checks if the 3rd value is a number between 0 and 100 inclusive, if correct it will create
   a 'record' with the respective values. *)
let parse line =
  match String.split_on_char ' ' line |> List.filter (fun s -> s <> "") with
  | firstname :: lastname :: score_str :: _ -> (
      try
        let score = int_of_string score_str in
        if score >= 0 && score <= 100 then Some { firstname; lastname; score }
        else None
      with Failure _ -> None)
  | _ -> None

(* This reads from the input channel and iterates over the lines, with each line becoming an 'entry'. *)
let rec read_file ic =
  try
    let line = input_line ic in
    let rest = read_file ic in
    match parse line with
    | Some entry -> entry :: rest
    | None -> rest
  with End_of_file ->
    close_in ic;
    []

(* Helper function for loading a file from disk. *)
let file_load input_file =
  try read_file (open_in input_file) with Sys_error _ -> []

(* Sorts entries by score record (descending), and then if equal, sorts by last name (ascending). *)
let rec sort_records lst =
  List.sort
    (fun a b ->
      let c = compare b.score a.score in
      if c <> 0 then c else compare a.lastname b.lastname)
    lst

(* String formatter for a list of records. *)
let print_records lst =
  List.iter
    (fun r -> Printf.printf "%d %s %s\n" r.score r.lastname r.firstname)
    lst

(* Input args from command line. *)
let () =
  match Array.to_list Sys.argv with
  | [ _; filename ] ->
      let records = file_load filename in
      let sorted = sort_records records in
      print_records sorted
  | _ -> Printf.printf "usage: %s <filename>\n" Sys.argv.(0)
