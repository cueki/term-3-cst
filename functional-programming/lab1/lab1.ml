(* Madison Lovett, A01292253
   Jan 21, 2026 *)

(* Pairs corresponding elements from two lists into a list of tuples.
   Stops when the shorter list ends. Non tail-recursive implementation. *)
let rec zip a_list b_list =
    match (a_list, b_list) with
    | ([], _) | (_, []) -> []
    | (head_a :: tail_a, head_b :: tail_b) -> (head_a, head_b) :: zip tail_a tail_b


(**/**)
let test_zip () =
    assert (zip [1; 2; 3] ['a'; 'b'; 'c'; 'd'] = [(1, 'a'); (2, 'b'); (3, 'c')]);
    assert (zip [] [1; 2; 3] = []);
    assert (zip [1; 2] [] = []);
    assert (zip [1] [2] = [(1, 2)])
(**/**)


(* Tail-recursive version of zip. Uses an accumulator and reverses
   the result at the end to maintain order. *)
let zip_tr a_list b_list =
    let rec aux a_list b_list acc =
        match (a_list, b_list) with
        | ([], _) | (_, []) -> List.rev acc
        | (head_a :: tail_a, head_b :: tail_b) -> aux tail_a tail_b ((head_a, head_b) :: acc)
        in aux a_list b_list []


(**/**)
let test_zip_tr () =
    assert (zip_tr [1; 2; 3] ['a'; 'b'; 'c'; 'd'] = [(1, 'a'); (2, 'b'); (3, 'c')]);
    assert (zip_tr [] [1; 2; 3] = []);
    assert (zip_tr [1; 2] [] = []);
    assert (zip_tr [1] [2] = [(1, 2)])
(**/**)


(* Splits a list of pairs into a pair of lists.
   Non tail-recursive implementation. *)
let rec unzip zip_list =
    match zip_list with
    | [] -> ([], [])
    | (a, b) :: tail_c ->
        let (a_list, b_list) =
        unzip tail_c in (a :: a_list, b :: b_list)


(**/**)
let test_unzip () =
    assert (unzip [(1, 'a'); (2, 'b'); (3, 'c')] = ([1; 2; 3], ['a'; 'b'; 'c']));
    assert (unzip [] = ([], []));
    assert (unzip [(1, 2)] = ([1], [2]));
    assert (unzip [(1, 4); (2, 5); (3, 6)] = ([1; 2; 3], [4; 5; 6]))
(**/**)


(* Tail-recursive version of unzip. Uses two accumulators for
   the first and second components, then reverses both at the end. *)
let unzip_tr zip_list =
    let rec aux zip_list acc_a acc_b =
    match zip_list with
    | [] -> (List.rev acc_a, List.rev acc_b)
    | (a, b) :: tail_c -> aux tail_c (a :: acc_a) (b :: acc_b)
    in aux zip_list [] []


(**/**)
let test_unzip_tr () =
    assert (unzip_tr [(1, 'a'); (2, 'b'); (3, 'c')] = ([1; 2; 3], ['a'; 'b'; 'c']));
    assert (unzip_tr [] = ([], []));
    assert (unzip_tr [(1, 2)] = ([1], [2]));
    assert (unzip_tr [(1, 4); (2, 5); (3, 6)] = ([1; 2; 3], [4; 5; 6]))
(**/**)


(* Helper function that checks if an element exists in a list.
   Returns true if found, false otherwise. *)
let rec memory exist lst =
    match lst with
    | [] -> false
    | head :: tail -> head = exist || memory exist tail


(* Removes duplicate elements from a list, keeping the last
   occurrence. Non tail-recursive implementation. *)
let rec dedup d_list =
    match d_list with
    | [] -> d_list
    | head :: tail ->
        let rest = dedup tail in
        if memory head rest then rest else head :: rest


(**/**)
let test_dedup () =
  assert (dedup [1; 2; 3] = [1; 2; 3]);
  assert (dedup [4; 4] = [4]);
  assert (dedup [1; 2; 1; 3] = [2; 1; 3])
(**/**)


(* Tail-recursive version of dedup. Uses an accumulator to build
   the result, checking if each element already exists before adding it. *)
let dedup_tr d_list =
    let rec aux d_list acc_d =
        match d_list with
        | [] -> List.rev acc_d
        | head :: tail ->
            if memory head acc_d then aux tail acc_d
            else aux tail (head :: acc_d)
    in aux d_list []


(**/**)
let test_dedup_tr () =
  assert (dedup_tr [1; 2; 3] = [1; 2; 3]);
  assert (dedup_tr [4; 4] = [4]);
  assert (dedup_tr [1; 2; 1; 3] = [1; 2; 3])
(**/**)


(* Executes all test functions. *)
let run_all_tests () =
    test_zip ();
    test_zip_tr ();
    test_unzip ();
    test_unzip_tr ();
    test_dedup ();
    test_dedup_tr ();
