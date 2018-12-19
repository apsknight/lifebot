<?php
class Query_insert extends CI_Model{
     function __construct() {
      parent::__construct();
      }



 	function insert($data){
 	 $this->db->insert('queries',$data);
 	
      
  }
 	}
?>  
      