(* Madison Lovett, A01292253
   Feb 4, 2026 *)

(* I am not sure if you wanted comments on each function or not but the code is essentially
   copied from bstree2.ml with slight modifications...*)

type ('k, 'v) kvtree = Leaf | Node of 'k * 'v * ('k, 'v) kvtree * ('k, 'v) kvtree

let kvtree_empty = Leaf

let kvtree_is_empty t = t = Leaf

let rec kvtree_find_opt k t =
  match t with
  | Leaf -> None
  | Node (k', v, l, _) when k < k' -> kvtree_find_opt k l
  | Node (k', _, _, r) when k > k' -> kvtree_find_opt k r
  | Node (_, v, _, _) -> Some v

let rec kvtree_add k v t =
  match t with
  | Leaf -> Node (k, v, Leaf, Leaf)
  | Node (k', v', l, r) when k < k' -> Node (k', v', kvtree_add k v l, r)
  | Node (k', v', l, r) when k > k' -> Node (k', v', l, kvtree_add k v r)
  | Node (_, _, l, r) -> Node (k, v, l, r)

let rec kvtree_remove_min t =
  match t with
  | Leaf -> failwith "kvtree_remove_min: empty tree"
  | Node (k, v, Leaf, r) -> (k, v, r)
  | Node (k, v, l, r) ->
    let (min_k, min_v, l') = kvtree_remove_min l in
    (min_k, min_v, Node (k, v, l', r))

let rec kvtree_remove k t =
  match t with
  | Leaf -> Leaf
  | Node (k', v', l, r) when k < k' -> Node (k', v', kvtree_remove k l, r)
  | Node (k', v', l, r) when k > k' -> Node (k', v', l, kvtree_remove k r)
  | Node (_, _, Leaf, r) -> r
  | Node (_, _, l, Leaf) -> l
  | Node (_, _, l, r) ->
    let (succ_k, succ_v, r') = kvtree_remove_min r in
    Node (succ_k, succ_v, l, r')

let kvtree_of_list lst =
  List.fold_left (fun acc (k, v) -> kvtree_add k v acc) Leaf lst
