package quiz;

/**
 *
 * @author LABRPL-11
 */
public class RunPegawai {
    public static void main(String[] args) {
        Pegawai pegawai1=new Pegawai();
        pegawai1.setName("Eza");
        pegawai1.setNIM("L200183178");
        System.out.println("Nama : " + pegawai1.getName());
        System.out.println("NIM : " + pegawai1.getNIM());
        System.out.println("Untuk mengetahui rincian gaji, masukan jabatan : " + "\n" +"1. Manajer Senior" + "\n" +"2. Manajer Junior");
        Pegawai pegawai2=new Pegawai(2);
    }    
}
