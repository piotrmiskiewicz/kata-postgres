package main

import (
    "database/sql"
    "fmt"
    _ "github.com/lib/pq"
    "os"
    "strconv"
    "time"
)

var loc *time.Location

func main() {

    loc, _ = time.LoadLocation("America/Chicago")

    t := time.Now().In(loc)
    fmt.Println(os.Getenv("TZ"))
    fmt.Println(t)
    fmt.Println(FormatTimestamp(t))
    t = t.UTC()
    fmt.Println(FormatTimestamp(t))
    os.Exit(0)

    url := "host=localhost port=5432 user=postgres password=Str0ngP@ssword dbname=postgres sslmode=disable timezone=America/Chicago"
    db, err := sql.Open("postgres", url)
    if err != nil {
        panic(err)
    }

    PrintDBTimezone(db)

    InsertInstance(db, "i12")

}

// FormatTimestamp formats t into Postgres' text format for timestamps.
func FormatTimestamp(t time.Time) string {
    // Need to send dates before 0001 A.D. with " BC" suffix, instead of the
    // minus sign preferred by Go.
    // Beware, "0000" in ISO is "1 BC", "-0001" is "2 BC" and so on
    bc := false
    if t.Year() <= 0 {
        // flip year sign, and add 1, e.g: "0" will be "1", and "-10" will be "11"
        t = t.AddDate((-t.Year())*2+1, 0, 0)
        bc = true
    }
    b := []byte(t.Format("2006-01-02 15:04:05.999999999Z07:00"))

    _, offset := t.Zone()
    offset %= 60
    if offset != 0 {
        // RFC3339Nano already printed the minus sign
        if offset < 0 {
            offset = -offset
        }

        b = append(b, ':')
        if offset < 10 {
            b = append(b, '0')
        }
        b = strconv.AppendInt(b, int64(offset), 10)
    }

    if bc {
        b = append(b, " BC"...)
    }
    return string(b)
}

func InsertInstance(db *sql.DB, id string) {
    now := time.Now().In(loc)
    _, err := db.Exec("insert into instances(instance_id, t1, t2) values($1, $2, $3);", id, now, now)
    if err != nil {
        panic(err)
    }
}

func PrintDBTimezone(db *sql.DB) {
    r, err := db.Query("SHOW timezone ;")
    if err != nil {
        panic(err)
    }
    var result string
    r.Next()
    r.Scan(&result)
    fmt.Println("Current DB timezone:", result)
    r.Close()
}
